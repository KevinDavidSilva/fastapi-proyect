from pydantic import BaseModel, EmailStr
from datetime import datetime

class Customer(BaseModel):
    id: int
    name: str
    description: str | None
    email: EmailStr
    age: int


class Trasaction(BaseModel):
    id: int
    amount: int
    description: str
    timestamp: datetime


class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Trasaction]
    total: int

    @property
    def ammount_total(self):
        return sum(transaction.amount for transaction in self.transactions)