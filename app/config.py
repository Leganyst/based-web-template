from fastapi import FastAPI

import secrets
import string

app = FastAPI()

# Конфигурация генерации JWT токенов
# Непосредственно секретный ключ
SECRET_KEY = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range (32))
# Алгоритм шифрования
ALGORITHM = "HS256"
# Время жизни токена доступа в минутах
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# Время жизни докена обновления в днях
REFRESH_TOKEN_EXPIRE_DAYS = 1
