"""A dummy 'model' that doesn't really do anything useful.
Used only to test building, tagging and pushing a Docker image."""
import json
import os
import sys

MODEL_NAME = os.getenv("MODEL_NAME", "dummy-model")
MODEL_VERSION = os.getenv("MODEL_VERSION", "0.1.0")

# Fake "weights"
WEIGHTS = {"w": 2.0, "b": 1.0}


def predict(x: float) -> float:
    return WEIGHTS["w"] * x + WEIGHTS["b"]


if __name__ == "__main__":
    x = float(sys.argv[1]) if len(sys.argv) > 1 else 3.0
    print(json.dumps({
        "model": MODEL_NAME,
        "version": MODEL_VERSION,
        "input": x,
        "prediction": predict(x),
    }))
