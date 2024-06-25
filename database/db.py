from sqlalchemy import create_engine
import os

# Конфигурационный файл (структура) для базы данных. Подгружает данные из
# переменных окружения, или использует по умолчанию, если их нет
class DatabaseConfig:
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASS = os.getenv("DB_PASS", "postgres")
    DB_NAME = os.getenv("DB_NAME", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")

try: 
    # Движок SQLAlchemy создаётся на основе Postgres и драйвера psycopg2
    engine = create_engine(
        f"postgresql+psycopg2://{DatabaseConfig.DB_USER}:{DatabaseConfig.DB_PASS}@{DatabaseConfig.DB_HOST}:{DatabaseConfig.DB_PORT}/{DatabaseConfig.DB_NAME}"
    )
except Exception as e:
    print("Failed to connect to the database: ", e)