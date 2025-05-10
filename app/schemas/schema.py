from pydantic import BaseModel

class Input(BaseModel):
    sentence: str
    foreign_word: str