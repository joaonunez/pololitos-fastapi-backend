import traceback
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from sqlmodel import SQLModel
from app.core.db import engine
from app.core import cloudinary_config
from app.routes.user_routes import router as user_router
from app.routes.service_routes import router as service_router
import app.models  # importa los modelos para crear las tablas

app = FastAPI()

origins = [
    "http://localhost:3000",  # Tu frontend en desarrollo
    # "https://tudominio.com",  # El dominio real en producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # Aquí se especifican los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],                # Métodos permitidos: GET, POST, etc.
    allow_headers=["*"],                # Encabezados permitidos
)

# Registra routers
app.include_router(user_router)
app.include_router(service_router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return PlainTextResponse(str(traceback.format_exc()), status_code=500)
