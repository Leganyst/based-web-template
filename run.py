from database.models.based import Base
from database.db import engine

from app.config import app
from app.routes.auth import auth

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(auth, prefix="/auth")