from fastapi import FastAPI

app = FastAPI()

users_db = [
    {"id": 1, "role": "admin", "name": "Musharraf"},
    {"id": 2, "role": "investor", "name": "Musharraf"},
    {"id": 3, "role": "customer", "name": "Musharraf"},

]

book_db = [
    {"id": 1, "userid": 2, "name": "Deep Work", "body": "Deep work book page 1440"},
    {"id": 2, "userid": 1, "name": "Rich Father", "body": "Rich Father book page 1840"},
    {"id": 3, "userid": 2, "name": "Data Since book", "body": "Data Since book page 1640"},
    {"id": 4, "userid": 4, "name": "Python cookbook", "body": "Python cookbook book page 1640"}
]


@app.get("/users/{userid}")
async def get_user(userid: int):
    return [user for user in users_db if user.get("id") == userid]


@app.get("/books")
async def books(limit: int = 1, offset: int = 0):
    return book_db[offset:][:limit]


@app.post("/users/{userid}")
async def user_change_name(userid: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == userid, users_db))[0]
    current_user["name"] = new_name
    return {"status_code": 200, "data": current_user}


