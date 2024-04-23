from fastapi import APIRouter
import logging

router = APIRouter()

@router.get("/health", name="Check-health")
def health():
    try:
        raise ValueError("Hello")
    except ValueError:
        logging.info("Hello")

    return "Ok"