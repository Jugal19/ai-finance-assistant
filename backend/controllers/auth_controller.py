from fastapi import HTTPException, status
from schemas.auth_schemas import RegisterRequest, LoginRequest, AuthResponse
from utils.auth import hash_password, verify_password, create_token
from database.connection import client
from datetime import datetime

class AuthController:

    @staticmethod
    async def register_user(request: RegisterRequest):
        users = client.finance.users

        # Check to see if user exists
        existing = await users.find_one({"email": request.email})
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")
        
        user = {
            "name": request.name,
            "email": request.email,
            "passwordHash": hash_password(request.password),
            "createdAt": datetime.utcnow()
        }

        await users.insert_one(user)

        token = create_token({"email": user["email"], "name": user["name"]})

        return AuthResponse(token=token, name=user["name"], email=user["email"])
    
    @staticmethod
    async def login_user(request: LoginRequest):
        users = client.finance.users

        user = await users.find_one({"email": request.email})
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        if not verify_password(request.password, user["passwordHash"]):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        token = create_token({"email": user["email"], "name": user["name"]})

        return AuthResponse(token=token, name=user["name"], email=user["email"])