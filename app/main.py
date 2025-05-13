from app.schemas.refine_word import RequestType, RequestDeleteType
from app.services.refine_word import refine_word
from app.services.delete_purified_word import delete_purified_word_service

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def refine_word_controller(request: RequestType):
    return await refine_word(request)

@app.delete("/")
async def delete_purified_word_controller(request: RequestDeleteType):
    return await delete_purified_word_service(request)