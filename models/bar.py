from pydantic import BaseModel

class Bar(BaseModel):
    data: list[int]
    label: str
    