from fastapi import APIRouter, Depends
from utils.auth_middleware import require_user
from controllers.dashboard_controller import DashboardController
router = APIRouter()

@router.get("/summary")
async def summary(user = Depends(require_user)):
    return await DashboardController.summary(user)