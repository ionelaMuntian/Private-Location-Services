# service_provider_app/app/modules/poi_search/scenarios/nearest_k.py
from fastapi import HTTPException

from ..engines.ckks_engine import CKKSEngine
from ..engines.concrete_engine import ConcreteEngine
from ..engines.plaintext_engine import PlaintextEngine
from ..repository import PoiRepository
from ..schemas import ServiceProviderNearestKRequest

repository = PoiRepository()


def get_engine(scheme: str):
    if scheme == "plaintext":
        return PlaintextEngine()
    if scheme == "ckks":
        return CKKSEngine()
    if scheme == "concrete":
        return ConcreteEngine()
    raise HTTPException(status_code=400, detail=f"Unsupported scheme: {scheme}")


def execute_nearest_k(request: ServiceProviderNearestKRequest) -> dict:
    if request.scheme == "plaintext":
        if request.plaintext_query is None:
            raise HTTPException(status_code=422, detail="plaintext_query is required for plaintext mode.")

        results = repository.get_by_category_nearest_k_plaintext(
            category=request.category,
            k=request.k,
            latitude_m=request.plaintext_query.latitude_m,
            longitude_m=request.plaintext_query.longitude_m,
        )
        return {
            "scheme": request.scheme,
            "results": results,
        }

    if request.scheme == "ckks":
        if request.encrypted_query is None:
            raise HTTPException(status_code=422, detail="encrypted_query is required for ckks mode.")

        candidates = repository.get_candidates_by_category(
            category=request.category,
            latitude_m=request.encrypted_query.metadata["query_latitude_m"],
            longitude_m=request.encrypted_query.metadata["query_longitude_m"],
            limit=max(request.k * 20, 200),
        )

        engine = get_engine("ckks")
        return engine.compute_nearest_k(
            category=request.category,
            k=request.k,
            query={
                "payload": request.encrypted_query.payload,
                "metadata": request.encrypted_query.metadata,
            },
            candidates=candidates,
        )

    raise HTTPException(
        status_code=501,
        detail="Only plaintext and ckks are enabled right now.",
    )