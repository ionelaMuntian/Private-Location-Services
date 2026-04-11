# service_provider_app/app/modules/poi_search/engines/base.py
from abc import ABC, abstractmethod


class ServiceProviderEngine(ABC):
    @abstractmethod
    def compute_nearest_k(self, category: str, k: int, query: dict, candidates: list[dict]) -> dict:
        pass