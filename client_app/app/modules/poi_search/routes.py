# client_app/app/modules/poi_search/routes.py
from fastapi import APIRouter

from .schemas import (
    CategoryListResponse,
    NearestKClientRequest,
    NearestKClientResponse,
)
from .service import PoiSearchClientService

router = APIRouter()
service = PoiSearchClientService()


@router.post("/nearest-k", response_model=NearestKClientResponse)
async def nearest_k_by_category(request: NearestKClientRequest):
    return await service.nearest_k_by_category(request)


@router.get("/categories", response_model=CategoryListResponse)
async def list_categories():
    return await service.list_categories()