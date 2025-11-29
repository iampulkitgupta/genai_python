from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    name: str    
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

# product = Product(name="Laptop", price=1200.50, quantity=2)
# print(product.total_price)

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(
        ...,
        ge=1,        
        description="Number of nights to book"
    )
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night

booking = Booking(user_id=1, room_id=101, nights=3, rate_per_night=10)
print(booking.total_amount)
print(booking.model_dump())

