from fastapi import APIRouter, Depends
from schemas.transaction_schemas import TransactionCreate
from controllers.transaction_controller import TransactionController
from utils.auth_middleware import require_user

router = APIRouter()

@router.post("/add")
async def add(data: TransactionCreate, user = Depends(require_user)):
    return await TransactionController.add_transaction(user, data)

@router.get("/monthly")
async def monthly(user = Depends(require_user)):
    return await TransactionController.get_monthly_summary(user)

@router.get("/yearly")
async def yearly(user = Depends(require_user)):
    return await TransactionController.get_yearly_summary(user)