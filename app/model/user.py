from pydantic import BaseModel, EmailStr
from typing import Optional

#respose for getAllUsers - It says which field we need to send to client
#then 
class UserResponse(BaseModel):
    id: str
    name: str
    gender: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    role: int
    image: Optional[str]
    deleted_at: Optional[str]
    expireAt: Optional[str]

    class Config:
        from_attributes = True
