# app/services/service_service.py
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.models.service_model import Service

def get_paginated_services(db: Session, page: int, size: int):
    total = db.scalar(select(func.count()).select_from(Service))
    
    stmt = (
        select(Service)
        .order_by(Service.id.desc())
        .offset(page * size)
        .limit(size)
    )
    results = db.scalars(stmt).all()

    return total, results
