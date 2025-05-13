from app.database import get_connection
    
async def select_join_purified_word(foreign_id: str):
    conn = await get_connection()
    
    async with conn.cursor() as cursor:
        sql = """
            SELECT p.purified_word FROM purified_word_tb p
            JOIN join_tb j ON p.purified_id = j.purified_id
            WHERE j.foreign_id = %s
        """

        await cursor.execute(sql, (foreign_id, ))
    
        purified_words = [row[0] for row in await cursor.fetchall()]

    conn.close()
    
    return purified_words

async def select_purified_id(purified_word: str):
    conn = await get_connection()
    
    async with conn.cursor() as cursor:
        sql = "SELECT * FROM purified_word_tb WHERE purified_word = %s"
        await cursor.execute(sql, (purified_word, ))
    
        purified_ids = [row[0] for row in await cursor.fetchall()]
    
    conn.close()
    
    return purified_ids

async def insert_purified_word(dify_response, foreign_id):
    conn = await get_connection()
    
    async with conn.cursor() as cursor:
        for purified_word in [word for values in dify_response.values() for word in values]:
            sql = "SELECT purified_id FROM purified_word_tb WHERE purified_word = %s"
            await cursor.execute(sql, (purified_word,))
            
            exist_purified_id = [row[0] for row in await cursor.fetchall()]
            
            if not exist_purified_id:
                # DB 에 순화어가 존재하지 않는 경우
                sql = "INSERT INTO purified_word_tb (purified_word) VALUES (%s)"
                await cursor.execute(sql, (purified_word, ))
                await conn.commit()
                
                purified_ids = await select_purified_id(purified_word)
                
                sql = "INSERT INTO join_tb (foreign_id, purified_id) VALUES (%s, %s)"
                for purified_id in purified_ids:
                    await cursor.execute(sql, (foreign_id, purified_id, ))
                    await conn.commit()
                
    conn.close()