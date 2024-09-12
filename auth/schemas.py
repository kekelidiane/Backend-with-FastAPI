from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


class User(BaseModel):
    username: str
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    phone: int
    address: str

class Participant(User):
    profession: str

    class Config:
        from_attributes = True

class Admin(User):
    roles: Optional[List[str]] = Field(default = None)

    class Config:
        from_attributes = True

class Super_Admin(User):
    roles: Optional[List[str]] = Field(default = None)

    class Config:
        from_attributes = True


class UserInDB(User):
    hashed_password: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

