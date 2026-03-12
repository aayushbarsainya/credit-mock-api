from fastapi import APIRouter
from database import supabase

router = APIRouter()

@router.get("/transactions/{customer_id}")
def get_transactions(customer_id: str):

    transactions = supabase.table("transactions")\
        .select("*")\
        .eq("customer_id", customer_id)\
        .execute()

    return {
        "transactions": transactions.data
    }