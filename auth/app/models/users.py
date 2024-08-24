from bson import ObjectId
from pydantic import BaseModel, Field, SecretStr, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from enum import Enum


class Role(str, Enum):
    donor = "Donor"
    beneficiary = "Beneficiary"


class UserBase(BaseModel):
    email: EmailStr = Field(max_length=255)
    is_verified: bool = False
    company_name: str = Field(max_length=255)
    name: str = Field(max_length=255)
    phone_number: PhoneNumber = Field()
    role: Role = Field()


class UserRegister(BaseModel):
    email: EmailStr = Field(max_length=255)
    password: SecretStr = Field(min_length=8, max_length=40)
    company_name: str = Field(max_length=255)
    name: str = Field(max_length=255)
    phone_number: PhoneNumber = Field()
    role: Role = Field()


class User(UserBase):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")

    class Config:
        orm_mode = True


class UserAdmin(User):
    is_superuser: bool = False
