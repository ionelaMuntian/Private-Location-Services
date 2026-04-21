# service_provider_app/app/modules/poi_search/service.py
from .repository import PoiRepository
from .schemas import (
    ConcreteCandidatesRequest,
    ConcreteEvaluationRequest,
    ServiceProviderNearestKRequest,
)
from .scenarios.nearest_k import execute_nearest_k
from ..poi_search.engines.core_concrete import (
    execute_concrete_candidates,
    execute_concrete_evaluation,
)

class PoiSearchServiceProviderService:
    def __init__(self):
        self.repository = PoiRepository()

    def nearest_k_by_category(self, request: ServiceProviderNearestKRequest) -> dict:
        return execute_nearest_k(request)

    def list_categories(self) -> dict:
        return {"categories": self.repository.list_categories()}

    def concrete_candidates(self, request: ConcreteCandidatesRequest) -> dict:
        return execute_concrete_candidates(request)

    def concrete_evaluate(self, request: ConcreteEvaluationRequest) -> dict:
        return execute_concrete_evaluation(request)