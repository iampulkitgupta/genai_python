from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        title="Employee Name",
        description="The name of the employee",
        min_length=3,
        max_length=50,
        examples=["Pulkit Gupta"]
    )
    department: Optional[str]=None
    salary: float = Field(
        ...,
        ge=10000,
        le=100000,
        description="The Annual salary of the employee in USD",
        examples=[50000]
    )

input_data = {"id": 1, "name": "Pulkit Gupta", "department": "IT", "salary": 50000}

class User(BaseModel):
    email: str = Field(
        ...,
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="A valid email address"
    )
    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="The age of the user"
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="The discount of the user"
    )

input_data = {"email": "pulkit.gupta@comviva.com", "age": 25, "discount": 10}

user = User(**input_data)
print(user)

# emp = Employee(**input_data)
# print(emp)