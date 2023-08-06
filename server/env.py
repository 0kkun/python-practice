import os


def _getenv(key: str, default: str = ""):
    env = os.environ.get(key)
    if env is None:
        return default
    return env


class Env:
    APP_ENV = _getenv("APP_ENV", "local")
    DEBUG_MODE  = _getenv("DEBUG_MODE", "False")
    LOG_LEVEL = _getenv("LOG_LEVEL", "debug")
    APP_URL = _getenv("APP_URL")