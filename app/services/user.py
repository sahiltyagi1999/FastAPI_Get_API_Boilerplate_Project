from app.db.user import get_all_users_repo,create_user_repo

async def get_all_users_service():
    # Any business logic can go here later
    return await get_all_users_repo()

async def create_user_service(payload):
    user_dict = payload.dict()
    new_user = await create_user_repo(user_dict)
    return new_user