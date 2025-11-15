from app.db.user import get_all_users_repo

async def get_all_users_service():
    # Any business logic can go here later
    return await get_all_users_repo()
