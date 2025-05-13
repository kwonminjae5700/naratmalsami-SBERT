from app.schemas.refine_word import RequestDeleteType
from app.crud.purified_word import delete_purified_word

async def delete_purified_word_service(request: RequestDeleteType):
    return await delete_purified_word(request.foreign_word, request.purified_word)