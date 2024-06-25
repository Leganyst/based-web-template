from datetime import datetime, timedelta, UTC
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_token(data: dict, expires_delta: timedelta = None) -> str:
    """Создает токен на основе данных и срока истечения

    Args:
        data (dict): Данные для шитья в токен
        expires_delta (timedelta, optional): Время жизни для токена. По умолчанию есть None.

    Returns:
        str: Строку-токен
    """
    
    # В словаре передается в data только те данные, которые надо хранить в токене
    # В данном случае это почта пользователя для его валидации
    # expire - срок истечения токена. Его мы тоже передадим при вызове, и это объект timedelta
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        # Если не передан, тогда по умолчанию срок истечения 15 минут
        expire = datetime.now(UTC) + timedelta(minutes=15)
    # Добавляем в словарь срок годности токена
    to_encode.update({"exp": expire})
    # И энкодим в JWT
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def validate_token(token: str) -> dict | None:
    """Валидация токена

    Args:
        token (str): Строка-токен

    Raises:
        JWTError: Ошибка в токене (отсутствие идентификатора)
        JWTError: Ошибка в токене (отсутствие срока годности)
        JWTError: Токен просрочен

    Returns:
        dict | None: Возвращает данные раскодированные из токена в виде словаря, либо ничего,
        если происходит ошибка. 
    """
    try:
        # Получаем словарь обратно
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # в sub (в функции при вызове) мы передаём идентификатор юзера 
        id: str = payload.get('sub')
        if id is None:
            # Если её нет
            raise JWTError("Token payload missing required failed")
        
        expiration = payload.get('exp')
        if expiration is None:
            # Если нет срока годности
            raise JWTError("Token payload missing expiration")
        
        # Вычисляем теперь срок истечения токена
        expire = datetime.fromtimestamp(expiration, tz=UTC)
        if datetime.now(UTC) > expire:
            raise JWTError("Token expired")
        # В конце концов, возвращаем раскодированный словарь из токена
        return payload
    except JWTError:
        return None

def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))) -> dict:
    """Получение текущего пользователя из токена

    Args:
        token (str, optional): Строка токена. По умолчанию Depends(OAuth2PasswordBearer(tokenUrl="token")).

    Returns:
        dict: Если токен валиден, возвращается словарь. В нем возвращается уникальный
        идентификатор пользователя.
        Если токен невалиден или его нет, возвращается словарь с ключом result=False
        и информацией для выброса ошибки 401.
    """
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # Получаем словарь из токена
    payload = validate_token(token)
    # Если валиден и есть ключ sub, тогда мы возвращаем просто идентификатор пользователя
    if payload is not None and "sub" in payload:
        payload.update({"result": True})
        return payload
    else:
        return {
            "result": False,
            "exception": credentials_exception
            }
        