from app.database import get_connection
    
def get_join_purified_word(foreign_word):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = """
        SELECT p.purified_word FROM purified_word_tb p 
        JOIN join_tb j ON p.purified_id = j.purified_id 
        JOIN foreign_word_tb f ON f.foreign_id = j.foreign_id 
        WHERE f.foreign_word = %s
    """

    cursor.execute(sql, (foreign_word[0],))
    
    row = cursor.fetchone()

    return row