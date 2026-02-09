from pydantic import BaseModel


class User(BaseModel):
    pass


class UserRequest(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: str
