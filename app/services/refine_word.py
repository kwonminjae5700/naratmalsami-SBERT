from app.schemas.refine_word import RequestType, ResponseType
from app.crud.purified_word import select_join_purified_word, insert_purified_word
from app.crud.foreign_word import select_foreign_id
from app.ai.kr_sbert import sentence_embedding
from app.ai.dify import dify

async def use_dify(foreign_id, foreign_word, sentence):
    dify_response = await dify(foreign_word, sentence)
    insert_purified_word(dify_response, foreign_id)
    
    return dify_response

async def refine_word(request: RequestType):
    sentence = request.sentence
    
    for foreign_word in request.foreign_word:
        foreign_id = select_foreign_id(foreign_word)
        
        if foreign_id:
            # 외래어가 DB 에 있는 경우
            purified_words = select_join_purified_word(foreign_id)
            
            if purified_words:
                # 외래어에 대한 순화어가 DB 에 있는 경우
                purified_embedding =  sentence_embedding(foreign_word, sentence, purified_words)
                
                if purified_embedding['score'] >= 0.7:
                    # DB 에 있는 순화어의 의미가 상통한 경우
                    return purified_embedding
                else:
                    # DB 에 있는 순화어의 의미가 상통하지 않은 경우
                    return await use_dify(foreign_id, foreign_word, sentence)
                    
            else:
                # 외래어에 대한 순화어가 DB 에 없는 경우
                return await use_dify(foreign_id, foreign_word, sentence)

        else:
            # 외래어가 DB 에 없는 경우
            print("J")