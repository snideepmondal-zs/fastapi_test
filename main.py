from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Adjust this to your Angular app's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Define the labels and datasets
labels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012']
datasets = [
    { "data": [65, 59, 80, 81, 56, 55, 40], "label": "Series A" },
    { "data": [28, 48, 40, 19, 86, 27, 90], "label": "Series B" }
]

# Combine labels and datasets into a single structure
data = {
    "labels": labels,
    "datasets": datasets
}

@app.get("/")
def root():
    return data
