from database.connection import client
from datetime import datetime

class DashboardController:

    @staticmethod
    async def summary(user):
        transactions = client.finance.transactions

        now = datetime.now()
        month = now.month
        year = now.year

        cursor = transactions.find({
            "userEmail": user["email"],
            "$expr": {
                "$and":
                [
                    {"$eq": [{"$month": "$date"}, month]},
                    {"$eq": [{"$year": "$date"}, year]}
                ]
            }
        })

        docs = await cursor.to_list(None)

        income = sum(t["amount"] for t in docs if t["type"] == "income")
        expenses = sum(t["amount"] for t in docs if t["type"] == "expense")

        # category breakdown
        category_totals = {}
        for t in docs:
            if t["type"] == "expense":
                category_totals[t["category"]] == category_totals.get(t["category"], 0) + t["amount"]

        return {
            "income": income,
            "expenses": expenses,
            "net": income - expenses,
            "categories": category_totals
        }