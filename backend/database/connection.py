import motor.motor_asyncio
from os import getenv
from dotenv import load_dotenv

load_dotenv()

client = None

async def connect_to_mongo():
    global client
    uri = getenv("MONGODB_URI")
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    print("MongoDB connected successfully")