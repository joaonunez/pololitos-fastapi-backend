from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables desde .env

DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el engine de SQLAlchemy (usado por SQLModel)
engine = create_engine(DATABASE_URL, echo=True)

# Función para inyectar sesión de base de datos (usado con Depends)
def get_db():
    with Session(engine) as session:
        yield session
