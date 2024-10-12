from fastapi import FastAPI
import asyncio
from plate_validator.event_listener import event_listener
from plate_validator.routers import plate
from app.plate_validator.database import redis_client, initialize_redis
from app.plate_validator.event_listener import event_listener
from app.plate_validator.routers.plate import router as plate_router
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    
    loop = asyncio.get_event_loop()
    loop.create_task(event_listener())

app.include_router(plate.router)


app = FastAPI(lifespan=lambda: lifespan_handler())

async def lifespan_handler():
    
    initialize_redis()
    event_listener()
    yield

    redis_client.close()


app.include_router(plate_router)