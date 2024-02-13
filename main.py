import os
import dotenv
import psycopg2
from fastapi import FastAPI
import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger('')
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('log.log', mode='a', maxBytes=50000000, backupCount=5, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)

logger.addHandler(handler)

app = FastAPI(
    title="pereval",
    version="1.0.0",
    description="pereval",
)


# @app.get("/pereval_added/{pereval_id}")
# async def pereval_added(pereval_id: int):
#     return {"pereval_id": pereval_id}


def main() -> None:
    # dotenv.load_dotenv()
    # logger.info('Читаем .env')
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
