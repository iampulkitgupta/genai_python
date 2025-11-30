from pydantic import BaseModel
from typing import Optional, Union

class Company(BaseModel):
    name: str
    address: Optional[List['Address']] = None
    phone_number: Optional[str] = None

class Employee(BaseModel):
    name: str
    address: Optional[List['Address']] = None
    phone_number: Optional[str] = None
    company: Optional['Company'] = None

class Text(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union['Text', 'ImageContent']]

class Country(BaseModel):
    name: str
    code: str
    population: int
    capital: str
    neighbors: Optional[List['Country']] = None

class State(BaseModel):
    name: str
    code: str
    population: int
    capital: str
    country: Optional['Country'] = None

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    state: State
    zip_code: str

class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address] = []

