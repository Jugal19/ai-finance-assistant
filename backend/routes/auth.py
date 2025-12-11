from fastapi import APIRouter, Header, HTTPException
from schemas.auth_schemas import RegisterRequest, LoginRequest
from controllers.auth_controller import AuthController
from utils.auth import decode_token

router = APIRouter()

@router.post("/register")
async def register(req: RegisterRequest):
    return await AuthController.register_user(req)

@router.post("/login")
async def login(req: LoginRequest):
    return await AuthController.login_user(req)

@router.get("/me")
async def me(Authorization: str | None = Header(None)):
    if not Authorization:
        raise HTTPException(status_code=401, detail="Missing token")
    
    token = Authorization.replace("Bearer ", "")
    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return {"user": payload}