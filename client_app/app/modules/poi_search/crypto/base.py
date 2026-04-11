# C:\Users\Mariana Ionela\MATERII\AN 4 - UTCN\LICENTA - PYTHON\client_app\app\modules\poi_search\crypto\base.py
from abc import ABC, abstractmethod


class ClientCryptoAdapter(ABC):
    @abstractmethod
    def prepare_query(self, latitude: float, longitude: float, k: int) -> dict:
        pass

    @abstractmethod
    def parse_response(self, response_data: dict) -> list[dict]:
        pass