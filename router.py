from sqlalchemy import select, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from fastapi import APIRouter, Depends
from models import pereval_added, users
from schemas import SubmitData, AddPereval, PerevalAdded
import json
import sys

pereval_router = APIRouter(
    prefix="/pereval",
)

submitdata_router = APIRouter(
    prefix="/submitdata",
)

@pereval_router.get("/get_perevals_added", tags=["Получить данные обо всех перевалах"])
async def get_pereval_added(session: AsyncSession = Depends(get_async_session)):
    """
    Asynchronous function to get the perevals added.
    Args:
        session (AsyncSession): The async session to use for the database operation.
    Returns:
        str: A string representation of the query result or None if the result is empty.
    """
    query = select(pereval_added)
    result = await session.execute(query)
    return str(result.all() or None)


@pereval_router.get("/get_pereval_added/{pereval_id}", tags=["Получить данные о конкретном перевале"])
async def get_pereval_added(pereval_id: int, session: AsyncSession = Depends(get_async_session)):
    """
    Retrieves the pereval added with the specified pereval_id using the given session.
    Returns the pereval added as a string or None if not found.
    """
    query = select(pereval_added).where(pereval_added.c.id == pereval_id)
    result = await session.execute(query)
    return str(result.all() or None)


possible_status = ["new", "pending", "accepted", "rejected"]


@pereval_router.post("/addpereval", tags=["Добавить данные о перевале"])
async def addpereval(pereval_added_scheme: AddPereval, session: AsyncSession = Depends(get_async_session)):
    """
        Asynchronous function for adding a pereval entry to the database.

        Parameters:
        - pereval_added_scheme: AddPereval - the data of the pereval to be added
        - session: AsyncSession - the async session for communicating with the database

        Returns:
        - dict: status indicating the success of the operation
    """
    new_pereval = insert(pereval_added).values(json.loads(pereval_added_scheme.json()))
    await session.execute(new_pereval)
    await session.commit()
    return {"status": "ok"}


@pereval_router.post("/submitdata/", tags=["Принять информацию о перевале"])
async def submitdata(submitdata: SubmitData, session: AsyncSession = Depends(get_async_session)):
    """
    Asynchronous function for submitting data to the database.
    Parameters:
    - submitdata: SubmitData object containing data to be submitted
    - session: AsyncSession for asynchronous database operations
    Returns:
    - Dictionary with status "error" if the submitdata status is not in possible_status, otherwise returns {"status": "ok"}
    """
    if submitdata.status not in possible_status:
        return {"status": "error"}
    else:
        update_status = update(pereval_added).where(pereval_added.c.id == submitdata.id).values(status=submitdata.status)
        await session.execute(update_status)
        await session.commit()
        return {"status": "ok"}


@submitdata_router.get("/submitdata/{pereval_id}", tags=["Получить расширенную информацию о перевале"])
async def get_pereval_added(pereval_id: int, session: AsyncSession = Depends(get_async_session)):
    """
    Retrieve the pereval data added with the specified pereval_id.

    Args:
        pereval_id (int): The ID of the pereval data to retrieve.
        session (AsyncSession, optional): The async session to use for the database operation. Defaults to the result of get_async_session.
    Returns:
        str: A string representation of the retrieved pereval data or None if no data is found.
    """
    query = select(pereval_added).where(pereval_added.c.id == pereval_id)
    result = await session.execute(query)
    return str(result.all() or None)


@submitdata_router.get("/", tags=["Получить информацию о данных пользователя"])
async def get_data_by_user(user_email: str, session: AsyncSession = Depends(get_async_session)):
    """
    Retrieve data added by user by their email address.
    Args:
        user_email (str): The email address of the user.
        session (AsyncSession, optional): The async session for the database. Defaults to Depends(get_async_session).
    Returns:
        str: A string representation of the query result or None if no data is found.
    """
    user_id = select(users.c.id).where(users.c.email == user_email)
    query = select(pereval_added).where(pereval_added.c.user_id == user_id)
    result = await session.execute(query)
    return str(result.all() or None)

@submitdata_router.patch("/submitdata/{pereval_id}", tags=["Редактировать информацию о перевале"])
async def submitdata(submitdata: PerevalAdded, session: AsyncSession = Depends(get_async_session)):
    """
    Update information about a mountain pass in the database.
    Args:
        submitdata (PerevalAdded): The data to be updated.
        session (AsyncSession): The asynchronous database session.
    Returns:
        dict: A dictionary with the updated state or an error message.
    """
    if submitdata.status not in possible_status:
        return {"status": "error"}
    else:
        update_pereval = update(pereval_added).where(pereval_added.c.id == submitdata.id).values(json.loads(submitdata.json()))
        try:
            await session.execute(update_pereval)
            await session.commit()
            return {"state": 1}
        except:
            await session.rollback()
            error_description = str(sys.exc_info()[1])
            return {"state": 0, "message": error_description}
