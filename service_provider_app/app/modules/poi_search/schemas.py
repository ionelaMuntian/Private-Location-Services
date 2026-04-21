# service_provider_app/app/modules/poi_search/schemas.py
from typing import Any, List, Literal
from pydantic import BaseModel, Field, model_validator


SchemeType = Literal["plaintext", "ckks", "concrete"]


class EncryptedLocationPayload(BaseModel):
    payload: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class PlaintextLocationPayload(BaseModel):
    latitude_m: float
    longitude_m: float


class ServiceProviderNearestKRequest(BaseModel):
    category: str
    k: int = Field(..., gt=0, le=200)
    scheme: SchemeType
    encrypted_query: EncryptedLocationPayload | None = None
    plaintext_query: PlaintextLocationPayload | None = None

    @model_validator(mode="after")
    def validate_payload_for_scheme(self):
        if self.scheme == "plaintext" and self.plaintext_query is None:
            raise ValueError("plaintext_query is required when scheme='plaintext'")
        if self.scheme in {"ckks", "concrete"} and self.encrypted_query is None:
            raise ValueError(f"encrypted_query is required when scheme='{self.scheme}'")
        return self


class PoiResult(BaseModel):
    id: int
    name: str
    category: str
    latitude: float
    longitude: float
    distance_km: float


class EncryptedPoiResult(BaseModel):
    id: int
    name: str
    category: str
    latitude: float
    longitude: float
    encrypted_distance: str


class CandidatePoiItem(BaseModel):
    id: int
    name: str
    category: str
    latitude: float
    longitude: float
    lat_m: float
    lon_m: float


class ConcreteCandidatesRequest(BaseModel):
    category: str
    k: int = Field(..., gt=0, le=200)
    latitude_m: float
    longitude_m: float


class ConcreteCandidatesResponse(BaseModel):
    category: str
    k: int
    candidates: List[CandidatePoiItem]


class ConcreteEvaluationItem(BaseModel):
    id: int
    name: str
    category: str
    latitude: float
    longitude: float
    public_args_b64: str


class ConcreteEvaluationRequest(BaseModel):
    evaluation_keys_b64: str
    requested_k: int
    items: List[ConcreteEvaluationItem]


class ConcreteEvaluationResultItem(BaseModel):
    id: int
    name: str
    category: str
    latitude: float
    longitude: float
    encrypted_distance: str


class ConcreteEvaluationResponse(BaseModel):
    scheme: SchemeType
    encrypted_results: List[ConcreteEvaluationResultItem]
    metadata: dict[str, Any]


class ServiceProviderNearestKResponse(BaseModel):
    scheme: SchemeType
    results: List[PoiResult] | None = None
    encrypted_results: List[EncryptedPoiResult] | None = None
    metadata: dict[str, Any] | None = None


class CategoryListResponse(BaseModel):
    categories: List[str]