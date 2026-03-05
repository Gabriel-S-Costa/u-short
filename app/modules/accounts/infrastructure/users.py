import uuid
from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: int | None = Field(primary_key=True, default=None)
    code: uuid.UUID = Field(default_factory=uuid.uuid4, index=True, unique=True)
    created_at: datetime | None = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default_factory=datetime.now(timezone.utc))
    deleted_at: datetime | None = Field(default=None)
    name: str = Field(max_length=255)
    email: str = Field(max_length=255, index=True, unique=True)
    password: str = Field(max_length=255)
    is_active: bool = Field(default=True)
