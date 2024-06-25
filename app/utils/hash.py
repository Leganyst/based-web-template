from sqlalchemy import select
from sqlalchemy.orm import Session

from database.db import engine
from database.models.user import User

import bcrypt

def generate_password_hash(password: str) -> str:
    """Генерирует хэш пароля

    Args:
        password (str): принимает строку пароля

    Returns:
        str: возвращает строку хэша пароля
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def validate_password_hash(password: str, id: str) -> bool:
    """Проверяет хэш пароля

    Args:
        password (str): Принимает строку пароля
        id (str): любой идентификатор для пользователя  

    Returns:
        bool: возвращает True, если пароль совпадает с хэшем, иначе False
    """
    with Session(engine) as session:
        user = session.execute(select(User).where(User.id == id)).scalars().one_or_none()
        if user is None:
            return False
        password_bytes = password.encode('utf-8')
        stored_password_bytes = user.password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, stored_password_bytes)