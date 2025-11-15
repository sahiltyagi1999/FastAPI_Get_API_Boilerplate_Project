from pydantic import BaseModel, EmailStr
from typing import Optional

#respose for getAllUsers - It says which field we need to send to client
#then 
class UserResponse(BaseModel):
    name: Optional[str] = None #made optional
    email: Optional[str] = None
    gender: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    role: Optional[int]
    image: Optional[str]
    deleted_at: Optional[str]
    expireAt: Optional[str]

    class Config:
        from_attributes = True


class CreateUserRequest(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[str] = None
    role: int = 1
    image: Optional[str] = None