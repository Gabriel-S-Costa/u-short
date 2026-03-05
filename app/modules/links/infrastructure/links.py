from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Link(SQLModel, table=True):
    __tablename__ = 'links'

    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(max_length=255, index=True, unique=True)
    created_at: datetime | None = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default_factory=datetime.now(timezone.utc))
    deleted_at: datetime | None = Field(default=None)
    user_id: int = Field(foreign_key='users.id')
    url: str = Field(max_length=255)
    is_active: bool = Field(default=True)
