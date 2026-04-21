# client_app/app/modules/poi_search/schemas.py
from typing import Literal, List

from pydantic import BaseModel, Field


SchemeType = Literal["plaintext", "ckks", "concrete"]


class NearestKClientRequest(BaseModel):
    category: str = Field(..., examples=["bank", "cafe", "supermarket"])
    k: int = Field(..., gt=0, le=200)
    latitude_m: float = Field(..., description="Projected metric latitude-like coordinate (EPSG:3857 Y)")
    longitude_m: float = Field(..., description="Projected metric longitude-like coordinate (EPSG:3857 X)")
    scheme: SchemeType = "plaintext"


class PoiItem(BaseModel):
    id: int
    name: str
    category: str
    latitude: float
    longitude: float
    distance_km: float


class NearestKClientResponse(BaseModel):
    scheme: SchemeType
    category: str
    k: int
    results: List[PoiItem]


class CategoryListResponse(BaseModel):
    categories: List[str]