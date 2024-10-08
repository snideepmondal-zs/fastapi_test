from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.data import data as data
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Adjust this to your Angular app's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.mount("/static", StaticFiles(directory="database"), name="static")

@app.get("/")
def root():
    return data()