from fastapi import APIRouter

router_say_hello = APIRouter(prefix='/say')


@router_say_hello.get('/hello')
async def say_hello():
    return {"message": "Hello"}
