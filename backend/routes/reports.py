from fastapi import APIRouter, Depends
from utils.auth_middleware import require_user
from controllers.report_controller import ReportController

router = APIRouter()

@router.get("/monthly")
async def monthly(user = Depends(require_user)):
    return await ReportController.generate_report(user)