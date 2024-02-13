import os
import dotenv
import psycopg2
from fastapi import FastAPI


app = FastAPI(
    title="pereval",
    version="1.0.0",
    description="pereval",
)


# @app.get("/pereval_added/{pereval_id}")
# async def pereval_added(pereval_id: int):
#     return {"pereval_id": pereval_id}


def main() -> None:
    # try:
    #     with psycopg2.connect(
    #         host=os.environ["FSTR_DB_HOST"],
    #         port=os.environ["FSTR_DB_PORT"],
    #         user=os.environ["FSTR_DB_LOGIN"],
    #         password=os.environ["FSTR_DB_PASS"],
    #         dbname="pereval",
    #     ) as connection:
    #         logger.info('Подключение к БД прошло успешно')
    #         print(connection)
    #         connection.autocommit = True
    #         with connection.cursor() as cursor:
    #             cursor.execute("UPDATE pereval_added SET status = 'new' WHERE id = 1")
    #         with connection.cursor() as cursor:
    #             cursor.execute("SELECT * FROM pereval_added")
    #             rows = cursor.fetchall()
    #             print(rows)
    pass
    # except psycopg2.OperationalError as e:
    #     logger.error('Не удалось подключиться к БД')
    #     print(e)


if __name__ == "__main__":
    main()
