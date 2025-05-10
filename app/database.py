import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    global conn
    conn = None
    
    if conn is None or not conn.is_connected():
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            port=os.getenv("DB_PORT"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        
    return conn