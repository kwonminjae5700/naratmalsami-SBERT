import pandas as pd
import sys
import re
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.database import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()

    path = '/Users/kwon5700/naratmalsami-sbert/data/raw/naratmalsami-data.tsv'
    pattern = re.compile(r"[^a-zA-Z가-힣, ]+")

    df = pd.read_csv(path, sep='\t', usecols=['다듬을 말', '다듬은 말'])
    
    cursor.execute("SELECT foreign_id FROM foreign_word_tb ORDER BY foreign_id DESC LIMIT 1")
    row = cursor.fetchone()
    foreign_id = row[0]
    # foreign_id = 0
    
    cursor.execute("SELECT purified_id FROM purified_word_tb ORDER BY purified_id DESC LIMIT 1")
    row = cursor.fetchone()
    korean_id = row[0]
    # korean_id = 0
    
    for i in range(len(df)):
        foreign = re.sub(pattern, '', df.iloc[i, 0])
        korean = re.sub(pattern, '', df.iloc[i, 1])
        
        foreign_add = []
        korean_add = []
        
        if foreign and korean:
            for data in foreign.split(', '):
                foreign_id += 1
                foreign_add.append({'data': data, 'id': foreign_id})
                
                cursor.execute(f"INSERT INTO foreign_word_tb (foreign_word) VALUES ('{data}')")
                conn.commit()
                
            for data in korean.split(', '):
                korean_id += 1
                korean_add.append({'data': data, 'id': korean_id})
                
                cursor.execute(f"INSERT INTO purified_word_tb (purified_word) VALUES ('{data}')")
                conn.commit()
                
            for foreign_data in foreign_add:
                for korean_data in korean_add:
                    print(f"{foreign_data['id']} : {korean_data['id']}")
                    print(f"{foreign_data['data']} : {korean_data['data']}")
                    cursor.execute(f"INSERT INTO join_tb (foreign_id, purified_id) VALUES ('{foreign_data['id']}', '{korean_data['id']}')")
                    conn.commit()
            
                    

except Exception as e:
    print(f"Error: {e}")
    
    
finally:
    conn.close()
    cursor.close()