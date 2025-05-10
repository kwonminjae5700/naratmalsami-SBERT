
from sentence_transformers import SentenceTransformer, util
import torch
from typing import List

model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

def sentence_embedding(foreign_word: str, sentence: str, purified_words: List[str]):
    purified_sentences = [
        sentence.replace(
            foreign_word, purified_word
        ) for purified_word in purified_words
    ]
    
    original_embedding = model.encode(sentence, convert_to_tensor=True)
    purified_embedding = model.encode(purified_sentences, convert_to_tensor=True)
    
    cosine_scores = util.cos_sim(original_embedding, purified_embedding)
    best_idx = torch.argmax(cosine_scores)
    

    return {
        "purified_word": purified_words[best_idx],
        "score": cosine_scores[0][best_idx].item()
    }
