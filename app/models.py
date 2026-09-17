# Import every ORM model here so Alembic can discover its metadata.
from app.modules.users.models import User

__all__ = ["User"]
