import motor.motor_asyncio
from os import getenv

client = None
async def connect_to_mongo():
    global client
    uri = getenv("MONGODB_URI")
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    print("MongoDB connected!")