from fastapi import APIRouter
from database import supabase

router = APIRouter()

@router.get("/autodebits/{customer_id}")
def get_autodebits(customer_id: str):

    failures = supabase.table("autodebit_failures")\
        .select("*")\
        .eq("customer_id", customer_id)\
        .execute()

    return {
        "failures": failures.data
    }