from pydantic import BaseModel
from typing import List, Dict

class Base(BaseModel):
    target_id: str
    sentence: str
    
class RequestType(Base):
    foreign_word: List[str]
    
class ResponseType(Base):
    refineWord: Dict[str, List[str]]
