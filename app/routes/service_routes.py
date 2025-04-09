# app/routes/service_routes.py
from fastapi import APIRouter, Depends, Query, HTTPException
from math import ceil
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas.service_schema import ServiceOut
from app.services.service_service import (get_paginated_services,
                                        search_services_by_name ,
                                        get_my_services,
                                        get_service_by_id
                                        )

from app.auth.jwt_bearer import get_current_user_id

router = APIRouter(prefix="/api/services", tags=["Services"])

@router.get("/paginated", response_model=dict)
def paginated_services(
    page: int = Query(0, ge=0),
    size: int = Query(8, gt=0),
    db: Session = Depends(get_db)
):
    total, services = get_paginated_services(db, page, size)

    return {
        "totalPages": ceil(total / size),
        "totalElements": total,
        "pageNumber": page,
        "pageSize": size,
        "content": [ServiceOut.from_orm(service) for service in services],
    }

@router.post("/search", response_model=dict)
def search_services(
    keyword: str = Query(..., min_length=1),
    page: int = Query(0, ge=0),
    size: int = Query(8, gt=0),
    db: Session = Depends(get_db)
):
    total, services = search_services_by_name(db, keyword, page, size)

    return {
        "totalPages": ceil(total / size),
        "totalElements": total,
        "pageNumber": page,
        "pageSize": size,
        "content": [ServiceOut.from_orm(service) for service in services],
        "searchTerm": keyword
    }

@router.get("/my-services", response_model=dict)
def get_my_services_route(
    page: int = Query(0, ge=0),
    size: int = Query(4, gt=0),
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    total, services = get_my_services(db, user_id, page, size)
    return {
        "totalPages": ceil(total / size),
        "totalElements": total,
        "pageNumber": page,
        "pageSize": size,
        "content": [ServiceOut.from_orm(service) for service in services],
    }

@router.get("/public/service/{id}", response_model=ServiceOut)
def public_service_by_id(id:int, db:Session = Depends(get_db)):
    service = get_service_by_id(db, id)
    if not service:
        raise HTTPException(status_code=404, detail="servicio no encontrado")
    return ServiceOut.from_orm(service)