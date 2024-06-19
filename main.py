import uvicorn
from fastapi import FastAPI
from routers.say_hello import router_say_hello

app = FastAPI()

app.include_router(router_say_hello)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=False)
