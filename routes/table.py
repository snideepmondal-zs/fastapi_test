from fastapi import APIRouter, Query,Path
from models.table import Table, Name
import os
import json
from fastapi import HTTPException

table = APIRouter()

FILE_PATH = os.getcwd() + "\\database\\tableData.json"

def read_json_file():
    if not os.path.exists(FILE_PATH):
        return {"results": []}
    
    with open(FILE_PATH, 'r') as file:
        return json.load(file)

# Function to write JSON data to the file
def write_json_file(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)


@table.get("/table")
def tableGet():
    return read_json_file()

@table.post("/table")
def add_entry(entry: Table):
    data = read_json_file()
    new_entry = entry.model_dump()
    new_entry["item_id"] = data["results"][-1]["item_id"] + 1
    data["results"].append(new_entry)
    write_json_file(data)
    return {"message": "Entry added successfully"}

@table.put("/table/{item_id}")
def updateTable(*, item_id: int = Path(..., ge=1), entry:Table, q:str|None = Query(None, max_length=10)):
    data = read_json_file()
    item_found = False
    
    # Iterate through the results to find and update the item
    for i in range(len(data["results"])):
        if data["results"][i].get("item_id") == item_id:
            # Update the entry
            updated_entry = entry.dict()
            updated_entry["item_id"] = item_id
            data["results"][i] = updated_entry
            item_found = True
            break
    
    if not item_found:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")
    
    # Write updated data back to the file
    write_json_file(data)
    
    return {"message": "Entry updated successfully"}