from fastapi import FastAPI
from app.schemas.schema import Input

app = FastAPI()

@app.post("/")
def vector(input: Input):
    return {"message":input}