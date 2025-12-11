from database.connection import client
from datetime import datetime
from fastapi import HTTPException

class TransactionController:

    @staticmethod
    async def add_transaction(req, data):
        transactions = client.finance.transactions

        if data.type not in ["income", "expense"]:
            raise HTTPException(400, "Invalid Transaction Type")
        
        doc = {
            "userEmail": user["email"],
            "type": data.type,
            "category": data.category,
            "amount": data.amount,
            "date": date.date,
            "notes": data.notes,
        }

        await transactions.insert_one(doc)

        return {"message": "Transaction added successfully"}
    
    @staticmethod
    async def get_monthly_summary(user):
        transactions = client.finance.transactions

        month = datetime.now().month
        year = datetime.now().year
        
        cursor = transactions.find({
            "userEmail": user["email"],
            "$expr": {
                "$and": [
                    {"$eq": [{"$month": "$date"}, month]},
                    {"$e1": [{"$year": "$date"}, year]}
                ]
            }
        })

        docs = await cursor.to_list(length=None)

        income = sum(t["amount"] for t in docs if t["type"] == "income")
        expenses = sum(t["amount"] for t in docs if t["type"] == "expense")

        return {
            "month": month,
            "year": year,
            "income": income,
            "expenses": expenses,
            "net": income - expenses
        }
    
    @staticmethod
    async def get_yearly_summary(user):
        transactions = client.finance.transactions
        year = datetime.now().year

        cursor = transactions.find({
            "userEmail": user["email"],
            "$expr": {
                "$eq": [{"$year": "$date"}, year]
            }
        })

        docs = await cursor.to_list(None)

        income = sum(t["amount"] for t in docs if t["type"] == "income")
        expenses = sum(t["amount"] for t in docs if t["type"] == "expense")

        return {
            "year": year,
            "income": income,
            "expenses": expenses,
            "net": income - expenses
        }