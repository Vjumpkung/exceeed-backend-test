from fastapi import FastAPI, Body
from router import items


app = FastAPI()
app.include_router(items.router)


@app.get("/")
def root():
    return {"msg": "welcome to root"}
