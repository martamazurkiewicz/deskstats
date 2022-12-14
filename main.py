from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class StatName(str, Enum):
    desk_hight = "desk"
    screen_usage = "screen"
    numerical_board_usage = "numerical"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/stats/{stat_name}")
async def get_stat(stat_name: StatName):
    if stat_name is StatName.desk_hight:
        return {"model_name": stat_name, "message": ""}

    if stat_name.value == "screen":
        return {"model_name": stat_name, "message": ""}

    return {"model_name": stat_name, "message": "H"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}
