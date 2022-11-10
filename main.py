from enum import Enum
from fastapi import FastAPI

api = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@api.get("/")
async def root():
    return {"message": "Hello, world"}


@api.get("/items/{item_id}")
async def read_item(item_id: int, needy: str, skip: int, limit: int | None = None):
    return {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}


@api.get("/users/me")
async def read_user_me():
    return {"user": "the current user"}


@api.get("/users/{user_ud}")
async def read_user(user_id: int):
    return {"user": user_id}


@api.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "resnet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@api.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
