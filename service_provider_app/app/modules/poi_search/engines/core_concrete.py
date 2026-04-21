from fastapi import HTTPException

from ..repository import PoiRepository
from ..schemas import (
    ConcreteCandidatesRequest,
    ConcreteEvaluationRequest,
)
from ....core.concrete_server_runtime import ConcreteServerRuntime

repository = PoiRepository()


def execute_concrete_candidates(request: ConcreteCandidatesRequest) -> dict:
    candidates = repository.get_candidates_by_category(
        category=request.category,
        latitude_m=request.latitude_m,
        longitude_m=request.longitude_m,
        limit=max(request.k * 20, 200),
    )

    normalized = []
    for item in candidates:
        normalized.append(
            {
                "id": item["id"],
                "name": item["name"],
                "category": item["category"],
                "latitude": item["latitude"],
                "longitude": item["longitude"],
                "lat_m": item["lat_m"],
                "lon_m": item["lon_m"],
            }
        )

    return {
        "category": request.category,
        "k": request.k,
        "candidates": normalized,
    }


def execute_concrete_evaluation(request: ConcreteEvaluationRequest) -> dict:
    try:
        runtime = ConcreteServerRuntime()
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Concrete server runtime unavailable: {exc}",
        ) from exc

    encrypted_results = []

    for item in request.items:
        encrypted_distance = runtime.run_distance(
            serialized_evaluation_keys_b64=request.evaluation_keys_b64,
            serialized_public_args_b64=item.public_args_b64,
        )

        encrypted_results.append(
            {
                "id": item.id,
                "name": item.name,
                "category": item.category,
                "latitude": item.latitude,
                "longitude": item.longitude,
                "encrypted_distance": encrypted_distance,
            }
        )

    return {
        "scheme": "concrete",
        "encrypted_results": encrypted_results,
        "metadata": {
            "requested_k": request.requested_k,
            "candidate_count": len(request.items),
            "top_k_on_client": True,
        },
    }