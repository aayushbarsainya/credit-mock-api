from fastapi import FastAPI
from routes import customers, transactions, loans, credit

app = FastAPI()

app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(loans.router)
app.include_router(credit.router)

@app.get("/")
def home():
    return {"message":"Mock Credit Intelligence API"}