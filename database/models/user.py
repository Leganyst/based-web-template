from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database.models.based import Base

class User(Base):
    __tablename__ = "users"
    
    """
    Базовое определение таблицы пользователей
    Содержит поля:
    - id: идентификатор пользователя
    - name: имя пользователя
    - password: хэш пароля пользователя
    """
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
