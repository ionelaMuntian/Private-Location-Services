# C:\Users\Mariana Ionela\MATERII\AN 4 - UTCN\LICENTA - PYTHON\client_app\app\infrastructure\http_client.py
import httpx
from fastapi import HTTPException

from ..core.config import settings


async def get_from_service_provider(path: str) -> dict:
    async with httpx.AsyncClient(timeout=300.0) as client:
        try:
            response = await client.get(f"{settings.service_provider_base_url}{path}")
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"Service provider unavailable: {exc}") from exc

        if response.status_code >= 400:
            try:
                detail = response.json()
            except Exception:
                detail = {"detail": response.text}
            raise HTTPException(status_code=response.status_code, detail=detail)

        return response.json()


async def post_to_service_provider(path: str, payload: dict) -> dict:
    async with httpx.AsyncClient(timeout=300.0) as client:
        try:
            response = await client.post(
                f"{settings.service_provider_base_url}{path}",
                json=payload,
            )
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"Service provider unavailable: {exc}") from exc

        if response.status_code >= 400:
            try:
                detail = response.json()
            except Exception:
                detail = {"detail": response.text}
            raise HTTPException(status_code=response.status_code, detail=detail)

        return response.json()