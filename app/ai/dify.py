import httpx
import json
import re
import os

DIFY_URL = os.getenv("DIFY_URL")
DIFY_KEY = os.getenv("DIFY_KEY")

async def dify(foreign_word: str, sentence: str):
    print("dify")
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{DIFY_URL}/workflows/run",
            headers={
                "Authorization": f"Bearer {DIFY_KEY}",
            },
            json={
                "inputs": {
                    "foreign_words": foreign_word,
                    "text_to_replace": sentence,
                },
                "response_mode": "blocking",
                "user": "asdfasdf-123"
            },
            timeout=90
        )
    
    response = response.json()
    matches = re.findall(r'\{(.*?)\}', response['data']['outputs']['text'], re.DOTALL)
    
    json_data = json.loads('{' + (matches[0] if matches else '{}') + '}')

    return json_data
    