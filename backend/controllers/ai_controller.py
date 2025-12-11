from utils.ai_client import get_insights
from database.connection import client
from datetime import datetime

class AIController:

    @staticmethod
    async def insights(user):
        transactions = client.finance.transactions

        month = datetime.now().month
        year = datetime.now().year

        cursor = transactions.find({
            "userEmail": user["email"],
            "$expr": {
                "$and": [
                    {"$eq": [{"$month": "$date"}, month]},
                    {"$eq": [{"$year": "$date"}, year]}
                ]
            }
        })

        docs = await cursor.to_list(None)

        text = "Here are my transactions this month:\n"
        for t in docs:
            text += f"- {t['date']}: {t['type']} {t['amount']} on {t['category']}\n"

        prompt = text + "\nGive me personalized insights to improve my finances."

        ai_output = await get_insights(prompt)

        return {"insights": ai_output}