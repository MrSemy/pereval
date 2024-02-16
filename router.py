from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from fastapi import APIRouter, Depends
from models import pereval_added
from schemas import SubmitData

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


possible_status = ["new", "pending", "accepted", "rejected"]


@router.post("/submitdata/")
async def submitdata(submitdata: SubmitData, session: AsyncSession = Depends(get_async_session)):
    if submitdata.status not in possible_status:
        return {"status": "error"}
    else:
        update_status = update(pereval_added).where(pereval_added.c.id == submitdata.id).values(status=submitdata.status)
        await session.execute(update_status)
        await session.commit()
        return {"status": "ok"}



# @router.post("/submitdata/{pereval_id:int}/{set_status:str}")
# async def submitdata(pereval_id: int, set_status: str, session: AsyncSession = Depends(get_async_session)):
#     update_status = update(pereval_added).where(pereval_added.c.id == pereval_id).values(status=set_status)
#     await session.execute(update_status)
#     await session.commit()
#     return {"status": "ok"}
