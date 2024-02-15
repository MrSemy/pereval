import psycopg2
from sqlalchemy import select, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
import config
from database import get_async_session
from fastapi import APIRouter, Depends
from models import pereval_added


router = APIRouter(
    prefix="/pereval",
    tags=["pereval"],
)


@router.get("/get_perevals_added")
async def get_pereval_added(session: AsyncSession = Depends(get_async_session)):
    query = select(pereval_added)
    result = await session.execute(query)
    return str(result.all() or None)


@router.get("/get_pereval_added/{pereval_id}")
async def get_pereval_added(pereval_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(pereval_added).where(pereval_added.c.id == pereval_id)
    result = await session.execute(query)
    return str(result.all() or None)


@router.post("/submitdata/{pereval_id:int}/{set_status:str}")
async def submitdata(pereval_id: int, set_status: str, session: AsyncSession = Depends(get_async_session)):
    update_status = update(pereval_added).where(pereval_added.c.id == pereval_id).values(status=set_status)
    await session.execute(update_status)
    await session.commit()
    return {"status": "ok"}
