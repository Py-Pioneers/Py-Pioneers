def calculate_total_bill(amount: float, tip_percent: int) -> float:
    amount= float(amount)
    tip_percent= float(tip_percent)
    if not(0<= amount<= 10000):
        raise ValueError("Amount must be between 0 and 10000")
    if not(0<= tip_percent<= 100):
        raise ValueError("Tip percent must be between 0 and 100")
    total= amount+(amount * tip_percent/ 100)
    return round(total, 2)
