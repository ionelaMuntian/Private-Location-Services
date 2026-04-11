# client_app/app/modules/poi_search/crypto/ckks_client.py
import tenseal as ts

from .base import ClientCryptoAdapter
from ....core.encryption import (
    CKKSContextManager,
    deserialize_ckks_vector,
    serialize_ckks_vector,
)


class CKKSClientAdapter(ClientCryptoAdapter):
    """
    Real CKKS implementation:
    - client encrypts [latitude_m, longitude_m]
    - server computes encrypted squared distances against clear POI coordinates
    - client decrypts returned encrypted scores and picks top-k
    """

    def prepare_query(self, latitude: float, longitude: float, k: int) -> dict:
        full_context = CKKSContextManager.create_full_context()

        query_vector = [float(latitude), float(longitude)]
        encrypted_query = serialize_ckks_vector(ts.ckks_vector(full_context, query_vector))

        return {
            "plaintext_query": None,
            "encrypted_query": {
                "payload": encrypted_query,
                "metadata": {
                    "public_context": CKKSContextManager.serialize_public_context(full_context),
                    "secret_context": CKKSContextManager.serialize_secret_context(full_context),
                    "query_encoding": "lat_m_lon_m_vector",
                    "distance_metric": "squared_euclidean_meters",
                    "top_k_on_client": True,
                    "requested_k": k,
                    "query_latitude_m": float(latitude),
                    "query_longitude_m": float(longitude),
                },
            },
        }

    def parse_response(self, response_data: dict) -> list[dict]:
        metadata = response_data["metadata"]
        secret_context = CKKSContextManager.load_secret_context(metadata["secret_context"])

        scored_items = []
        for item in response_data["encrypted_results"]:
            encrypted_score = deserialize_ckks_vector(secret_context, item["encrypted_distance"])
            decrypted = encrypted_score.decrypt()

            if isinstance(decrypted, list):
                score = float(decrypted[0])
            else:
                score = float(decrypted)

            scored_items.append(
                {
                    "id": item["id"],
                    "name": item["name"],
                    "category": item["category"],
                    "latitude": item["latitude"],
                    "longitude": item["longitude"],
                    "distance_km": round((max(score, 0.0) ** 0.5) / 1000.0, 4),
                }
            )

        scored_items.sort(key=lambda x: x["distance_km"])
        requested_k = int(metadata["requested_k"])
        return scored_items[:requested_k]