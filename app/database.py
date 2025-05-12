import aiomysql
from dotenv import load_dotenv
import os

load_dotenv()

async def get_connection():
    conn = await aiomysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        port=int(os.getenv("DB_PORT")),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME")
    )
    
    return conn