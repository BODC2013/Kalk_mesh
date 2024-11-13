from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

class r(BaseModel):
    a: int
    b: int
    c: Optional[int] = Field(default=0)
    d: Optional[int] = Field(default=0)
    e: Optional[int] = Field(default=0)
app = FastAPI()
def u(instance: r) -> int:
    return instance.a + instance.b + (instance.c or 0) + (instance.d or 0) + (instance.e or 0)

@app.post("/sum")
def get_sum(values: r):
    result = u(values)
    return {"sum": result}


#
#
# app = FastAPI()
#
#
# class StaskAdd(BaseModel):
#     name: str
#     description: Optional[str] = None
#
# class STask(StaskAdd):
#     id: int
#
# tasks = []
# @app.post("/tasks")
# async def add_task(
#         task: Annotated[StaskAdd, Depends()]
# ):
#     tasks.append(task)
#     return {"ok": True}
#
#
# # class Task(BaseModel):
# #     name: str
# #     description: Optional[str] = None
# #
# # @app.get("/tasks")
# # def get_task():
# #     task = Task(name="QWER")
# #     return {"fack": task}
