from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    age: int
    address: Optional[Address] = None
    phone_numbers: List[str] = []

user = User(id=1, name="John Doe", age=30, address=Address(street="123 Main St", city="Anytown", state="CA", zip_code="12345"), phone_numbers=["123-456-7890", "098-765-4321"])
print(user)
