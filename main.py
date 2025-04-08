import traceback
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from sqlmodel import SQLModel
from app.core.db import engine
from app.routes.user_routes import router as user_router

# 👇 Esto importa todos los modelos antes de crear las tablas
import app.models  

app = FastAPI()
app.include_router(user_router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return PlainTextResponse(str(traceback.format_exc()), status_code=500)