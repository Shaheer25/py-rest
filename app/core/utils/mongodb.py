import motor.motor_asyncio
from pymongo import MongoClient
from starlette.config import Config

config = Config()

MONGO_URL = config.get("MONGO_URL", default="mongodb://rest_mongodb:27017")
DATABASE = config.get("DATABASE", default="rest")

client = MongoClient(MONGO_URL)
asyncio_client = motor.motor_asyncio.AsyncIOMotorClient(
    MONGO_URL, uuidRepresentation="standard"
)

db = client[DATABASE]
asyncio_db = asyncio_client[DATABASE]
