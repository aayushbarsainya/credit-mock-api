from fastapi import APIRouter
from database import supabase

router = APIRouter()

@router.get("/customers/{customer_id}")
def get_customer(customer_id: str):

    customer = supabase.table("customers")\
        .select("*")\
        .eq("customer_id", customer_id)\
        .execute()

    accounts = supabase.table("accounts")\
        .select("*")\
        .eq("customer_id", customer_id)\
        .execute()

    return {
        "customer": customer.data,
        "accounts": accounts.data
    }