from fastapi import FastAPI
from model import Input

app = FastAPI()

@app.post("/")
def vector(input: Input):
    return {"message":input}