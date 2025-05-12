from app.crud.purified_word import insert_purified_word
from app.ai.dify import dify

async def use_dify(foreign_id, foreign_word, sentence):
    dify_response = await dify(foreign_word, sentence)
    insert_purified_word(dify_response, foreign_id)
    
    return dify_response