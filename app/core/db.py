from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables del archivo .env

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definido en el archivo .env")

# Crea el motor de SQLAlchemy con SQLModel
engine = create_engine(DATABASE_URL, echo=True)

# Dependency para inyectar la sesión de base de datos
def get_db():
    with Session(engine) as session:
        yield session
