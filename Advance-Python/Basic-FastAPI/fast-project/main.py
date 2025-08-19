from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers.user_router import router as user_router
from db.database import Base, engine
app = FastAPI()

Base.metadata.create_all(bind=engine) # CREATE ALL THE TABLES

app.include_router(user_router)

@app.get("/")
async def setup_message():
    return JSONResponse(
        {
            "response":"application is working"
        }
    )