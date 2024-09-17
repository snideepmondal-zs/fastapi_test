from pydantic import BaseModel

class Name(BaseModel):
    title: str
    first: str
    last: str

class Table(BaseModel):
    gender: str
    email: str
    name: Name  # Use the nested model here
    cell: str