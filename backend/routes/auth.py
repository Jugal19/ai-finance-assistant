from fastapi import APIRouter, Header, HTTPException
from schemas.auth_schemas import RegisterRequest, LoginRequest
from utils.auth import decode_token

router = APIRouter()

@router.post("/register")
async def register(request: RegisterRequest):
    return await AuthController.register_user(request)

@router.post("/login")
async def login(request: LoginRequest):
    return await AuthController.login_user(request)

@router.get("/me")
async def get_me(Authorization: str | None = Header(None)):
    if not Authorization:
        raise HTTPException(status_code=401, detail="Missing token")
    
    token = Authorization.split("Bearer ")[-1]
    payload = decode_token(token)

    if not payload:
        raise HTTPException(stutus_code=401, detail="Invalid token")
    
    return {"user": payload}