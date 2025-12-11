from fastapi import APIRouter, Depends
from utils.auth_middleware import require_user
from controllers.ai_controller import AIController

router = APIRouter()

@router.get("/insights")
async def insights(user = Depends(require_user)):
    return await AIController.insights(user)