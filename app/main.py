from app.schemas.refine_word import RequestType
from app.services.refine_word import refine_word

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