from fastapi import HTTPException
from schemas.auth_schemas import RegisterRequest, LoginRequest
from utils.auth import hash_password, verify_password, create_token
from database.connection import client
from datetime import datetime

class AuthController:

    @staticmethod
    async def register_user(req: RegisterRequest):
        users = client.finance.users

        # Check if the email exists
        existing = await users.find_one({"email": req.email})
        if existing:
            raise HTTPException(400, "Email already exists")
        
        user_data = {
            "name": req.name,
            "email": req.email,
            "passwordHash": hash_password(req.password),
            "createdAt": datetime.utcnow()
        }

        # Saves the user
        await users.insert_one(user_data)

        # creating the token
        token = create_token({
            "email": user_data["email"],
            "name": user_data["name"]
        })


        return {
            "message": "User registered successfully",
            "token": token,
            "user": {
                "name": user_data["name"],
                "email": user_data["email"]
            }
        }
    
    @staticmethod
    async def login_user(req: LoginRequest):
        users = client.finance.users

        user = await users.find_one({"email": req.email})
        if not user:
            raise HTTPException(401, "Invalid email or password")
        
        if not verify_password(req.password, user["passwordHash"]):
            raise HTTPException(401, "Invalid email or password")
        
        # creating the token
        token = create_token({
            "email": user["email"],
            "name": user["name"]
        })

        return {
            "message": "User logged in successfully",
            "token": token,
            "user": {
                "name": user["name"],
                "email": user["email"]
            }
        }