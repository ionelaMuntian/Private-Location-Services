# client_app/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Client App - Trusted Side"
    service_provider_base_url: str = "http://127.0.0.1:8001"

    # CKKS / TenSEAL settings
    ckks_poly_modulus_degree: int = 8192
    ckks_coeff_mod_bit_sizes: str = "60,40,40,60"
    ckks_global_scale_bits: int = 40

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def ckks_coeff_mod_bit_sizes_list(self) -> list[int]:
        return [int(x.strip()) for x in self.ckks_coeff_mod_bit_sizes.split(",") if x.strip()]


settings = Settings()