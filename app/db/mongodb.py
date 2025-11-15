from motor.motor_asyncio import AsyncIOMotorClient
from app.config.config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)
db = client[settings.DB_NAME]
