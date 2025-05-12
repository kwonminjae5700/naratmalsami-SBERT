from app.database import get_connection

async def select_foreign_id(foreign_word: str):
    conn = await get_connection()
    
    async with conn.cursor() as cursor:
        sql = "SELECT foreign_id FROM foreign_word_tb WHERE foreign_word = %s"
        await cursor.execute(sql, (foreign_word, ))
    
        row = await cursor.fetchone()
    
    conn.close()
    
    return row[0] if row and row[0] is not None else None

async def insert_foreign_word(foreign_word: str):
    conn = await get_connection()
    async with conn.cursor() as cursor:
    
        sql = "INSERT INTO foreign_word_tb (foreign_word) VALUES (%s)"
        await cursor.execute(sql, (foreign_word, )) 
        await conn.commit()
    
    conn.close()