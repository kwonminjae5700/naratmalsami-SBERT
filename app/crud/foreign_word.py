from app.database import get_connection

def select_foreign_id(foreign_word: str):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "SELECT foreign_id FROM foreign_word_tb WHERE foreign_word = %s"
    cursor.execute(sql, (foreign_word, ))
    
    row = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return row[0] if row and row[0] is not None else None

def insert_foreign_word(foreign_word: str):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "INSERT INTO foreign_word_tb (foreign_word) VALUES (%s)"
    cursor.execute(sql, (foreign_word, )) 
    conn.commit()
    
    cursor.close()
    conn.close()