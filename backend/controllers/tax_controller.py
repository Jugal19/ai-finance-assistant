from utils.tax_calc import calculate_tax
from database.connection import client

class TaxController:

    @staticmethod
    async def calculate(user, income: float):
        taxes = calculate_tax(income)

        record = {
            "userEmail": user["email"],
            "income": income,
            "federalTax": taxes["federal"],
            "provincialTax": taxes["provincial"],
            "totalTax": taxes["total"]
        }

        await client.finance.tax_records.insert_one(record)

        return record