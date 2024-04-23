import logging

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", name="Check-health")
def health():
    try:
        raise ValueError("Hello")
    except ValueError:
        logging.info("Hello")

    return "Ok"
