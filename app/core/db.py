from sqlmodel import create_engine, Session
from app.core.config import settings

# Usamos el DATABASE_URL desde el objeto de configuración
DATABASE_URL = settings.DATABASE_URL

# Crea el motor de SQLAlchemy con SQLModel
engine = create_engine(DATABASE_URL, echo=True)

# Dependency de FastAPI para inyectar la sesión de base de datos
def get_db():
    with Session(engine) as session:
        yield session
