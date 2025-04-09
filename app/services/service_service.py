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

def search_services_by_name(db: Session, keyword: str, page: int, size: int):
    query = db.query(Service).filter(func.lower(Service.name).like(f"%{keyword.lower()}%"))
    total = query.count()
    services = query.order_by(Service.created_at.desc()).offset(page * size).limit(size).all()
    return total, services

def get_my_services(db: Session, user_id: int, page: int, size: int):
    query = db.query(Service).filter(Service.user_id == user_id)
    total = query.count()
    services = query.order_by(Service.created_at.desc()).offset(page * size).limit(size).all()
    return total, services