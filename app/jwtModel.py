from datetime import date
import uuid
from pydantic import BaseModel, Field, EmailStr


class UserSchema (BaseModel):
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    age: int = Field(...)
    country: str = Field(...)
    user_created_time: date = Field(...)
    is_active: bool = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "092806f3-2be7-4e16-984a-400175278b21",
                "username": "John Doe",
                "email": "john@gmail.com",
                "password": "123456",
                "age": 30,
                "country": "USA",
                "user_created_time": "2021-01-01",
                "is_active": True
            }
        }


class UserLoginSchema (BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                "password": "any"
            }
        }
