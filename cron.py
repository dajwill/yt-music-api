import asyncio
import requests
from fastapi_utilities import repeat_every

@repeat_every(seconds=60*10)
async def ping():
    await asyncio.sleep(1)
    response = requests.get('https://yt-music-api-d7kt.onrender.com/ping')
    print(response.json())