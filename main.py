from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello, world"}


@api.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@api.get("/users/me")
async def read_user_me():
    return {"user": "the current user"}


@api.get("/users/{user_ud}")
async def read_user(user_id: int):
    return {"user": user_id}
