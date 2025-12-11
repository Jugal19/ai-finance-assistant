def calculate_tax(income):
    # Simple tax calculation
    federal = income * 0.15
    provincial = income * 0.10

    return {
        "federal": round(federal, 2),
        "provincial": round(provincial, 2),
        "total": round(federal + provincial, 2)
    }