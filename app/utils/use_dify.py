from app.crud.purified_word import insert_purified_word
from app.ai.dify import dify
from app.utils.change_dify_type import change_dify_type

async def use_dify(foreign_id, foreign_word, sentence, target_id, fullsentence):
    dify_response = await dify(foreign_word, sentence)
    insert_purified_word(dify_response, foreign_id)
    
    return change_dify_type(response=dify_response, target_id=target_id, fullsentence=fullsentence)