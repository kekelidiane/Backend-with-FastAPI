from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, List

class User(BaseModel):

    email: EmailStr = Field(..., description="Adresse email valide")

    @field_validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError("L'email doit contenir un '@'.")
        return value