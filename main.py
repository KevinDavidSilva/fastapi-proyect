from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo
from models import Customer, Trasaction, Invoice



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, Kevin!"}

country_timezones = {
    "US": "America/New_York",
    "GB": "Europe/London",
    "IN": "Asia/Kolkata",
    "JP": "Asia/Tokyo",
    "AU": "Australia/Sydney"
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezo_str = country_timezones.get(iso)
    tz = ZoneInfo(timezo_str)
    return {"time": datetime.now(tz)}

@app.post("/customers/")
async def create_customer(customer_data: Customer):
    return customer_data

@app.post("/transactions/")
async def create_transaction(transaction_data: Trasaction):
    return transaction_data

@app.post("/invoices/")
async def create_invoice(invoice_data: Invoice):
    return invoice_data
