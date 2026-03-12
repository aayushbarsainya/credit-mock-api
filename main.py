from fastapi import FastAPI

from routes import customers
from routes import transactions
from routes import loans
from routes import credit
from routes import salary
from routes import autodebits

app = FastAPI(title="Mock Credit Intelligence API")

app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(loans.router)
app.include_router(credit.router)
app.include_router(salary.router)
app.include_router(autodebits.router)

@app.get("/")
def home():
    return {"message": "Mock Financial Data API"}