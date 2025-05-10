from app.schemas.refine_word import RequestType
from app.services.refine_word import refine_word

from fastapi import FastAPI
    
app = FastAPI()

@app.post("/")
async def vector(request: RequestType):
    return await refine_word(request)