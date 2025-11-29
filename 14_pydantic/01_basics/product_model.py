from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True    

input_data = {"id":1, "name":"Product 1", "price":10.99, "in_stock": True}

product = Product(**input_data)
print(product)
