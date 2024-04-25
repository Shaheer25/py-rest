import logging
import sys

from loguru import logger
from starlette.config import Config
from starlette.datastructures import Secret

from app.core.utils.logging import InterceptHandler

config = Config()


API_PREFIX = "/api"
VERSION = "0.1.0"
DEBUG: bool = config("DEBUG", cast=bool, default=False)
MQTT_SERVICE: bool = config("MQTT_SERVICE", cast=bool, default=False)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="")
PROJECT_NAME: str = config.get("PROJECT_NAME", default="py-rest")

# Logging Configuration
LOGGING = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING}])
