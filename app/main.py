from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configs.configs import DEBUG, PROJECT_NAME, VERSION
from app.routes.helath import router as health_router


def config_cors(app: FastAPI):
    """
    Enables CORS for diffrerent
    1. Origins
    2. methods
    3. Headers
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    config_cors(application)
    return application


app = get_application()


app.include_router(health_router, tags=["Check Health"], prefix="/api/v1/health")
