from app.schemas.refine_word import ResponseType, ErrorItem

from typing import Dict

def change_dify_type(response: Dict, target_id: str, fullsentence: str):
    return ResponseType(
        target_id=target_id,
        errors=[
            ErrorItem(
                code=1,
                origin_word=foreign_word,
                refine_word=refine_word,
                index=fullsentence.find(foreign_word)
            ) for foreign_word, refine_word in response.items()
        ]
    )