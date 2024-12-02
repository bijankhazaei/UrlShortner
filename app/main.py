from fastapi import FastAPI
from app.api.endpoints.url_shortener import router as url_router

app = FastAPI(title="URL Shortener API")

app.include_router(url_router, prefix="/api", tags=["URL Shortener"])