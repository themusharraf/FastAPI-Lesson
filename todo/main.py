from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


todo_list = []


@app.post("/todos/", response_model=TodoItem)
def create_todo_item(item: TodoItem):
    todo_list.append(item)
    return item


@app.get("/todos/", response_model=List[TodoItem])
def get_all_todo_items():
    return todo_list


@app.get("/todos/{item_id}", response_model=TodoItem)
def get_todo_item(item_id: int):
    item = next((item for item in todo_list if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/todos/{item_id}", response_model=TodoItem)
def update_todo_item(item_id: int, updated_item: TodoItem):
    index = next((index for index, item in enumerate(todo_list) if item.id == item_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    todo_list[index] = updated_item
    return updated_item


@app.delete("/todos/{item_id}")
def delete_todo_item(item_id: int):
    index = next((index for index, item in enumerate(todo_list) if item.id == item_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    todo_list.pop(index)
    return {"message": "Item deleted successfully"}
