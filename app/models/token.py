from pydantic import BaseModel, Field
from typing import Optional

class Token(BaseModel):
    """
    Представляет собой модель токена, содержит всегда access токен и возможно refresh, а так же тип токенов
    """
    access_token: str = Field(..., description="Токен доступа, используемый для аутентификации запросов.",
                              example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
    refresh_token: Optional[str] = Field(None, description="Необязательный токен обновления, используемый для получения нового токена доступа после его истечения.",
                                         example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
    tokens_type: str = Field(..., description="Тип токена, обычно используется для указания метода аутентификации.", example="Bearer")

