from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_Active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")}
    )

user = User(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    createdAt=datetime.now(),
    address=Address(street="123 Main St", city="Anytown", zip_code="12345"),
    tags=["developer", "pydantic"]
)

print(type(user))
result = user.model_dump()
print(type(result))
result_json = user.model_dump_json(indent=5)
print(type(result_json))
print(result)
