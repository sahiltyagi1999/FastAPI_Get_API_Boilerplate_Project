from fastapi import APIRouter
from typing import List
from app.model.user import UserResponse
from app.services.user import get_all_users_service

router = APIRouter() #This router is exported back to main.py where it is used as router for user

@router.get("/", response_model=List[UserResponse]) 
async def get_all_users():
    return await get_all_users_service()


#response_model tells FastAPI what the output structure of this API should look like.
#List[UserResponse] -> this gives response in array 

# UserResponse is something we tailored that we want only these fields and we will send these fileds to client
#this helps us to leave creds and confidential info behind