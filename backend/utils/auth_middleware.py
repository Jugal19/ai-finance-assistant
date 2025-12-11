from fastapi import Header, HTTPException
from utils.auth import decode_token

async def require_user(Authorization: str | None = Header(None)):
    if not Authorization:
        raise HTTPException(401, "Missing Authorization Header")
    
    token = Authorization.replace("Bearer ", "")
    payload = decode_token(token)

    if not payload:
        raise HTTPException(401, "Invalid or expired token")
    
    return payload