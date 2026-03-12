from fastapi import APIRouter
import random
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/transactions/{customer_id}")
def get_transactions(customer_id:str, days:int=90):

    categories = ["Food","Transport","Shopping","Bills","Entertainment"]

    transactions = []

    for i in range(days):

        transactions.append({
            "date":str(datetime.now()-timedelta(days=i)),
            "amount":random.randint(-2000,-50),
            "category":random.choice(categories),
            "merchant":"DemoMerchant"
        })

    return {
        "customer_id":customer_id,
        "transactions":transactions
    }