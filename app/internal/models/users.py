from datetime import datetime

from pydantic import BaseModel
from sqlmodel import Field


class User(BaseModel):
    id: int | None = Field(primary_key=True, unique=True, default=None)
    created_at: datetime | None = Field(default=None)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)
    name: str = Field(max_length=255)
    email: str = Field(max_length=255)
    is_active: bool = Field(default=True)


class UserRequest(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: str
