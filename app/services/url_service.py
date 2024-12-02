from sqlalchemy.orm import Session
from app.db.models import URL
from app.services.caching import cache_url, get_cached_url
from app.utils.hashing import generate_short_url
from app.schemas import URLResponse

async def create_short_url_service(original_url: str, db: Session) -> URLResponse:
    cached_url = await get_cached_url(original_url)
    if cached_url:
        return URLResponse(short_url=cached_url, original_url=original_url)

    short_url = generate_short_url(original_url)
    db_url = db.query(URL).filter(URL.original_url == original_url).first()
    if not db_url:
        db_url = URL(original_url=original_url, short_url=short_url)
        db.add(db_url)
        db.commit()
        db.refresh(db_url)

    await cache_url(short_url, original_url)
    return URLResponse(short_url=short_url, original_url=original_url)

async def get_original_url_service(short_url: str, db: Session) -> URLResponse:
    cached_url = await get_cached_url(short_url)
    if cached_url:
        return URLResponse(short_url=short_url, original_url=cached_url)

    db_url = db.query(URL).filter(URL.short_url == short_url).first()
    if not db_url:
        return None

    await cache_url(short_url, db_url.original_url)
    return URLResponse(short_url=short_url, original_url=db_url.original_url)