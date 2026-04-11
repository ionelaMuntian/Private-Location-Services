# service_provider_app/app/modules/poi_search/routes.py
from fastapi import APIRouter

from .schemas import (
    CategoryListResponse,
    ServiceProviderNearestKRequest,
    ServiceProviderNearestKResponse,
)
from .service import PoiSearchServiceProviderService

router = APIRouter()
service = PoiSearchServiceProviderService()


@router.post("/nearest-k", response_model=ServiceProviderNearestKResponse)
def nearest_k_by_category(request: ServiceProviderNearestKRequest):
    return service.nearest_k_by_category(request)


@router.get("/categories", response_model=CategoryListResponse)
def list_categories():
    return service.list_categories()