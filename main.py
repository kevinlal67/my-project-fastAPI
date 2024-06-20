import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers.say_hello import router_say_hello

app = FastAPI()

origins = [
    "http://localhost:3000",  # Your React app's URL
    "https://my-project-fastapi.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_say_hello)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run('main:app', host="0.0.0.0", port=port, reload=False)

