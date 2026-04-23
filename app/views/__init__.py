from fastapi import APIRouter

from .home import router as home_router
from .page_missing import router as page_missing_router

router = APIRouter()

router.include_router(home_router)
router.include_router(page_missing_router)
