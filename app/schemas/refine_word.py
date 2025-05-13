from pydantic import BaseModel
from typing import List, Dict

class Base(BaseModel):
    target_id: str
    sentence: str
    
class RequestType(Base):
    foreign_word: str
    fullsentence: str
    
class ErrorItem(BaseModel):
    code: int
    origin_word: str
    refine_word: List[str]
    index: int
    
class ResponseType(BaseModel):
    target_id: str
    errors: List[ErrorItem]

class RequestDeleteType(BaseModel):
    foreign_word: str
    purified_word: str