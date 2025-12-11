from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    type: str
    category: str
    amount: float
    date: datetime
    notes: str | None = None
