from app.schemas.refine_word import RequestType
from app.crud.refine_word import get_join_purified_word

from sentence_transformers import SentenceTransformer, util
import torch

model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

def refine_word(request: RequestType):
    join_purified_word = get_join_purified_word(request.foreign_word)
    
    return join_purified_word
        