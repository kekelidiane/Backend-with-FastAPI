from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


class User(BaseModel):
    username: str
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    phone: int
    address: str

class CreateUser(User): 
    password: str = Field(...)
    confirm_password: str = Field(...)

class UpdateUser(BaseModel):
    username: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int] = None
    address: Optional[str] = None
    password: Optional[str] = None
    confirm_password: Optional[str] = None


class UserInDB(User):
    hashed_password: str

    class Config:
        from_attributes = True