# concrete_client.py
from fastapi import HTTPException

from .base import ClientCryptoAdapter


class ConcreteClientAdapter(ClientCryptoAdapter):
    def prepare_query(self, latitude: float, longitude: float, k: int) -> dict:
        raise HTTPException(
            status_code=501,
            detail=(
                "Concrete/TFHE path is intentionally disabled for now. "
                "Use plaintext or ckks. Build Concrete as phase 2 after the CKKS path is stable."
            ),
        )

    def parse_response(self, response_data: dict) -> list[dict]:
        raise HTTPException(
            status_code=501,
            detail="Concrete/TFHE path is intentionally disabled for now.",
        )