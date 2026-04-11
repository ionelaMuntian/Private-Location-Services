# service_provider_app/app/modules/poi_search/service.py

from .repository import PoiRepository
from .schemas import ServiceProviderNearestKRequest
from .scenarios.nearest_k import execute_nearest_k


class PoiSearchServiceProviderService:
    def __init__(self):
        self.repository = PoiRepository()

    def nearest_k_by_category(self, request: ServiceProviderNearestKRequest) -> dict:
        return execute_nearest_k(request)

    def list_categories(self) -> dict:
        return {"categories": self.repository.list_categories()}