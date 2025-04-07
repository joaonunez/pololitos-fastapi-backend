# Pololitos - Backend en FastAPI

Este proyecto es una migración del backend desde Spring Boot hacia FastAPI. La idea es mantener el frontend intacto, replicando los endpoints existentes pero usando Python como backend.

---

## 🔧 Requisitos

- Python 3.8 o superior
- pip (viene con Python)
- Editor de código (VSCode, PyCharm, etc.)

---

## 🚀 Instrucciones de instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/pololitos-fastapi-backend.git
cd pololitos-fastapi-backend

python -m venv venv

source venv/Scripts/activate

venv\Scripts\activate

source venv/bin/activate

pip install fastapi uvicorn python-multipart python-jose[cryptography] passlib[bcrypt]
