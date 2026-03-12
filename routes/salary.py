from fastapi import APIRouter
from database import supabase

router = APIRouter()

@router.get("/salary/{customer_id}")
def get_salary(customer_id: str):

    salary = supabase.table("salary_history")\
        .select("*")\
        .eq("customer_id", customer_id)\
        .execute()

    return {
        "salary_history": salary.data
    }