from fastapi import APIRouter
from models.bar import Bar
from database.data import data
import json

bar = APIRouter()

@bar.get("/")
def root():
    print(data())
    return data();