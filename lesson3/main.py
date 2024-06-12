from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse
from typing import List
from models import users_db, book_db, Books, Users

app = FastAPI()


@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exe: ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exe.errors()})
    )


@app.get("/users/{user_id}", response_model=List[Users])
async def get_user(user_id: int):
    return [user for user in users_db if user.get("id") == user_id]


@app.post("/users/{user_id}")
async def user_change_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users_db))[0]
    current_user["name"] = new_name
    return {"status_code": 200, "data": current_user}


@app.post("/books")
async def add_book(book: List[Books]):
    book_db.append(book)
    return {"status_code": 200, "data": book_db}
