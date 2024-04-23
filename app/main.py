from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.helath import router as health_router
from app.configs.configs import API_PREFIX, DEBUG,PROJECT_NAME

def config_cors(app : FastAPI):
    """
    Enables CORS for diffrerent
    1. Origins
    2. methods
    3. Headers
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def get_application() -> FastAPI :
    application = FastAPI(
        title=PROJECT_NAME,
        debug=DEBUG,
        version='0.1.0'
    )
    config_cors(application)
    return application


app = get_application()


app.include_router(health_router, tags=["Check Health"], prefix="/api/v1/health")