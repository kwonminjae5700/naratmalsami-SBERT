from app.schemas.refine_word import RequestType, ResponseType, ErrorItem
from app.crud.purified_word import select_join_purified_word
from app.crud.foreign_word import select_foreign_id, insert_foreign_word
from app.ai.kr_sbert import sentence_embedding
from app.utils.use_dify import use_dify

async def refine_word(request: RequestType):
    target_id = request.target_id
    sentence = request.sentence
    fullsentence = request.fullsentence
    foreign_word = request.foreign_word
    print("start")

    foreign_id = select_foreign_id(foreign_word)
    
    if not foreign_id:
        # 만약 외래어가 없다면
        insert_foreign_word(foreign_word)
        foreign_id = select_foreign_id(foreign_word)
        
    purified_words = select_join_purified_word(foreign_id)
        
    if purified_words:
        print("외래어에 대한 순화어가 DB 에 있다면")
        # 외래어에 대한 순화어가 DB 에 있는 경우
        purified_embedding =  sentence_embedding(foreign_word, sentence, purified_words)
        print(purified_embedding)
        if purified_embedding['score'] >= 0.7:
            # DB 에 있는 순화어의 의미가 상통한 경우
            print("외래어에 대한 순화어의 의미가 상통하다면")
            return ResponseType(
                target_id=target_id,
                errors=[
                    ErrorItem(
                        code=1,
                        origin_word=foreign_word,
                        refine_word=purified_embedding['purified_word'],
                        index=fullsentence.find(foreign_word)
                    )
                ]
            )

            
            # DB 에 있는 순화어의 의미가 상통하지 않은 경우
            # 외래어가 DB 에 없는 경우
            # 외래어에 대한 순화어가 DB 에 없는 경우

        response = await use_dify(foreign_id, foreign_word, sentence)
    
        return ResponseType(
            target_id=target_id,
            errors=[
                ErrorItem(
                    code=1,
                    origin_word=key,
                    refine_word=value,
                    index=fullsentence.find(value)
                )
                for key, value in response.items()
            ]
        )