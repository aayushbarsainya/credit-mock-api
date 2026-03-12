from fastapi import APIRouter
from database import supabase

router = APIRouter()

@router.get("/credit/{customer_id}")
def get_credit(customer_id: str):

    cards = supabase.table("credit_cards")\
        .select("*")\
        .eq("customer_id", customer_id)\
        .execute()

    return {
        "cards": cards.data
    }