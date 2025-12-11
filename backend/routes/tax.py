from fastapi import APIRouter, Depends
from utils.auth_middleware import require_user
from controllers.tax_controller import TaxController

router = APIRouter()

@router.post("/calculate")
async def calculate_tax(income: float, user = Depends(require_user)):
    return await TaxController.calculate(user, income)