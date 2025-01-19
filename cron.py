import asyncio
from fastapi_utilities import repeat_every

@repeat_every(seconds=60 * 13)
async def ping():
    await asyncio.sleep(1)
    print("pong")