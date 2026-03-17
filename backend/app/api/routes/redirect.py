from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import get_db
from app.services.url_service import URLService

router = APIRouter()


@router.get("/{short_code}", summary="Redirect to original URL")
async def redirect(short_code: str, db: AsyncSession = Depends(get_db)) -> RedirectResponse:
    url = await URLService().get_by_short_code(short_code, db)
    if not url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short code not found")
    return RedirectResponse(url=url.original_url, status_code=status.HTTP_302_FOUND)
