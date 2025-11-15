from app.db.mongodb import db
from bson import ObjectId

usersModel = db["ed_users"]

def serialize_user(user):
    """Convert Mongo DB object → JSON safe format"""
    return {
        "id": str(user["_id"]),
        "name": user.get("name"),
        "gender": user.get("gender"),
        "email": user.get("email"),
        "phone": user.get("phone"),
        "role": user.get("role"),
        "image": user.get("image"),
        "deleted_at": user.get("deleted_at"),
        "expireAt": user.get("expireAt")
    }

async def get_all_users_repo():
    cursor = usersModel.find({})
    users = []
    async for user in cursor:
        users.append(serialize_user(user))
    return users
