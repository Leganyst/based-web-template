from pydantic import BaseModel, Field

class UserAPI(BaseModel):
    """
    Представляет собой модель пользователя в API, содержащую основные учетные данные пользователя.
    """
    display_name: str = Field(..., description="ФИО пользователя, используемое для идентификации на платформе.", example="Иван Иванов")
    id: str = Field(..., description="Уникальный идентификатор пользователя, используемый для идентификации в системе.", example="ivanov_ivan")
    # email: str = Field(..., description="Электронная почта пользователя, используемая как логин для доступа к системе.", example="ivan.ivanov@example.com")
    password: str = Field(..., description="Пароль для входа в систему. Должен быть надежным и содержать комбинацию букв и цифр.", example="SecurePassword123!")