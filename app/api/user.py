from fastapi import APIRouter
from typing import List
from app.model.user import UserResponse,CreateUserRequest
from app.services.user import get_all_users_service,create_user_service
from app.db.user import serialize_user


router = APIRouter() #This router is exported back to main.py where it is used as router for user

@router.get("/", response_model=List[UserResponse]) 
async def get_all_users():
    return await get_all_users_service()


#response_model tells FastAPI what the output structure of this API should look like.
#List[UserResponse] -> this gives response in array 

# UserResponse is something we tailored that we want only these fields and we will send these fileds to client
#this helps us to leave creds and confidential info behind


@router.post("/", response_model=UserResponse)
async def create_user(payload: CreateUserRequest):
    new_user = await create_user_service(payload)
    return serialize_user(new_user)