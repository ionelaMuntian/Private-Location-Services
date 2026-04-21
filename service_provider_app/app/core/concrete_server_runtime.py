import base64
from pathlib import Path

from concrete import fhe

BASE_DIR = Path(__file__).resolve().parents[2]
ARTIFACTS_DIR = BASE_DIR / "shared" / "concrete_artifacts"
SERVER_PATH = ARTIFACTS_DIR / "server.zip"


def _b64decode(data: str) -> bytes:
    return base64.b64decode(data.encode("utf-8"))


def _b64encode(data: bytes) -> str:
    return base64.b64encode(data).decode("utf-8")


class ConcreteServerRuntime:
    def __init__(self) -> None:
        if not SERVER_PATH.exists():
            raise FileNotFoundError(
                f"Concrete server artifact not found at {SERVER_PATH}. "
                "Run compile_distance_circuit.py first."
            )
        self.server = fhe.Server.load(SERVER_PATH)

    def run_distance(
        self,
        serialized_evaluation_keys_b64: str,
        serialized_public_args_b64: str,
    ) -> str:
        evaluation_keys = fhe.EvaluationKeys.deserialize(
            _b64decode(serialized_evaluation_keys_b64)
        )
        public_args = fhe.PublicArguments.deserialize(
            _b64decode(serialized_public_args_b64)
        )

        public_result = self.server.run(
            public_args,
            evaluation_keys,
        )

        return _b64encode(public_result.serialize())