# service_provider_app/app/modules/poi_search/engines/concrete_engine.py
from fastapi import HTTPException

from .base import ServiceProviderEngine


class ConcreteEngine(ServiceProviderEngine):
    def compute_nearest_k(self, category: str, k: int, query: dict, candidates: list[dict]) -> dict:
        raise HTTPException(
            status_code=501,
            detail=(
                "Concrete/TFHE is intentionally disabled for now. "
                "Implement it as phase 2 after plaintext and CKKS are benchmarked."
            ),
        )