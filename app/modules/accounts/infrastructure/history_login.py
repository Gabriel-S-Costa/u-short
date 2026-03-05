from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class HistoryLogin(SQLModel, table=True):
    __tablename__ = 'history_logins'

    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=datetime.now(timezone.utc), nullable=True)
    updated_at: datetime | None = Field(default_factory=datetime.now(timezone.utc), nullable=True)
    user_id: int = Field(foreign_key='users.id')
    ip_address: str | None = Field(default=None, max_length=50)
    user_agent: str | None = Field(default=None, max_length=255)
    is_success: bool = Field(default=True)
