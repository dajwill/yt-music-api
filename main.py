from typing import Union
from ytmusicapi import YTMusic
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from cron import ping

@asynccontextmanager
async def lifespan(app: FastAPI):
    await ping()
    yield

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ytmusic = YTMusic()
# ytmusic = YTMusic("oauth.json")

@app.get("/")
async def read_root():
    homeResult = ytmusic.get_home()
    return homeResult

@app.get("/search")
def search_youtube(q: str, limit: Union[int, None] = 20, filter: Union[str, None] = None):
    return ytmusic.search(
        q,
        filter,
        None,
        limit
    )

@app.get('/artist/{browse_id}')
def get_artist(browse_id: str):
    return ytmusic.get_artist(browse_id)

@app.get("/song/{video_id}")
def read_song(video_id: str):
    return ytmusic.get_song(video_id)

@app.get("/album/{browse_id}")
def get_album(browse_id: str):
    return ytmusic.get_album(browse_id)

@app.get('/ping')
def api_ping():
    return {"message": "Hello World"}