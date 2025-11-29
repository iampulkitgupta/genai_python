from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str
    
    @field_validator("first_name", "last_name")
    def validate_name(cls, v):
        if not v.isalpha():
            raise ValueError("Name must contain only alphabetic characters")
        return v.title()

class User(BaseModel):
    email: str

    @field_validator("email")
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Email must contain an @ symbol")
        return v

class Product(BaseModel):
    price: float #$4.44

    @field_validator("price", mode="before")
    def validate_price(cls, v):
        if isinstance(v, str):
            v = v.replace("$", "")
            return float(v)
        return v

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_date_range(self):
        if self.start_date >= self.end_date:
            raise ValueError("Start date must be before end date")
        return self

user = User(email="pulkit.gupta@comviva.com")
# print(user)

person = Person(first_name="pulkit", last_name="gupta")
# print(person)

product = Product(price="$4.44")
print(product)

try:
    daterange = DateRange(start_date="2025-11-29", end_date="2025-11-28")
    print(daterange)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)