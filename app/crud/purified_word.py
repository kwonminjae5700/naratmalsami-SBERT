from app.database import get_connection
from app.crud.foreign_word import select_foreign_id
    
def select_join_purified_word(foreign_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = """
        SELECT p.purified_word FROM purified_word_tb p
        JOIN join_tb j ON p.purified_id = j.purified_id
        WHERE j.foreign_id = %s
    """

    cursor.execute(sql, (foreign_id, ))
    
    purified_words = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    
    return purified_words

def select_purified_id(purified_word: str):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "SELECT * FROM purified_word_tb WHERE purified_word = %s"
    cursor.execute(sql, (purified_word, ))
    
    row = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return row[0] if row is not None else None

def insert_purified_word(dify_response, foreign_id):
    conn = get_connection()
    cursor = conn.cursor()
    print(dify_response)
    
    
    for purified_word in [word for values in dify_response.values() for word in values]:
        exist_purified_id = select_purified_id(purified_word)
        
        if not exist_purified_id:
            # DB 에 순화어가 존재하지 않는 경우
            print("존재하지 않는 경우")
            sql = "INSERT INTO purified_word_tb (purified_word) VALUES (%s)"
            cursor.execute(sql, (purified_word, ))
            conn.commit()
            
            purified_id = select_purified_id(purified_word)
            
            sql = "INSERT INTO join_tb (foreign_id, purified_id) VALUES (%s, %s)"
            cursor.execute(sql, (foreign_id, purified_id, ))
            conn.commit()
            
    cursor.close()
    conn.close()