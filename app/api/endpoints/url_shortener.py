from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.url_service import create_short_url_service, get_original_url_service
from app.schemas import URLCreate, URLResponse

router = APIRouter()

@router.post("/shorten", response_model=URLResponse)
async def create_short_url(payload: URLCreate, db: Session = Depends(get_db)):
    return await create_short_url_service(payload.original_url, db)

@router.get("/{short_url}", response_model=URLResponse)
async def get_original_url(short_url: str, db: Session = Depends(get_db)):
    result = await get_original_url_service(short_url, db)
    if not result:
        raise HTTPException(status_code=404, detail="URL not found")
    return result