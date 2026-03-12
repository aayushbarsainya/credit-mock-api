from fastapi import APIRouter
from database import supabase

router = APIRouter()

@router.get("/loans/{customer_id}")
def get_loans(customer_id: str):

    loans = supabase.table("loans")\
        .select("*")\
        .eq("customer_id", customer_id)\
        .execute()

    return {
        "loans": loans.data
    }