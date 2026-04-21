# client_app/app/modules/poi_search/scenarios/nearest_k.py
from fastapi import HTTPException

from ..crypto.ckks_client import CKKSClientAdapter
from ..crypto.concrete_client import ConcreteClientAdapter
from ..crypto.plaintext_client import PlaintextClientAdapter
from ..schemas import NearestKClientRequest
from ....infrastructure.http_client import post_to_service_provider


def get_client_adapter(scheme: str):
    if scheme == "plaintext":
        return PlaintextClientAdapter()
    if scheme == "ckks":
        return CKKSClientAdapter()
    if scheme == "concrete":
        return ConcreteClientAdapter()
    raise HTTPException(status_code=400, detail=f"Unsupported scheme: {scheme}")


async def execute_nearest_k(request: NearestKClientRequest) -> dict:
    adapter = get_client_adapter(request.scheme)

    if request.scheme == "concrete":
        prepared = adapter.prepare_query(
            latitude=request.latitude_m,
            longitude=request.longitude_m,
            k=request.k,
        )

        candidate_response = await post_to_service_provider(
            "/service/poi/concrete/candidates",
            {
                "category": request.category,
                "k": request.k,
                "latitude_m": request.latitude_m,
                "longitude_m": request.longitude_m,
            },
        )

        items = adapter.build_public_args_for_candidates(
            prepared["encrypted_query"]["metadata"],
            candidate_response["candidates"],
        )

        raw_response = await post_to_service_provider(
            "/service/poi/concrete/evaluate",
            {
                "evaluation_keys_b64": prepared["encrypted_query"]["metadata"]["evaluation_keys"],
                "requested_k": request.k,
                "items": items,
            },
        )

        parsed_results = adapter.parse_response(raw_response, prepared.get("local_state"))

        return {
            "scheme": request.scheme,
            "category": request.category,
            "k": request.k,
            "results": parsed_results,
        }

    prepared = adapter.prepare_query(
        latitude=request.latitude_m,
        longitude=request.longitude_m,
        k=request.k,
    )

    service_payload = {
        "category": request.category,
        "k": request.k,
        "scheme": request.scheme,
        "plaintext_query": prepared["plaintext_query"],
        "encrypted_query": prepared["encrypted_query"],
    }

    raw_response = await post_to_service_provider(
        "/service/poi/nearest-k",
        service_payload,
    )

    parsed_results = adapter.parse_response(raw_response, prepared.get("local_state"))

    return {
        "scheme": request.scheme,
        "category": request.category,
        "k": request.k,
        "results": parsed_results,
    }