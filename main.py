from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo
from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    description: str | None
    email: str
    age: int

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
