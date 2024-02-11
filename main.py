import os
import dotenv
import psycopg2
import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger('')
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('log.log', mode='a', maxBytes=50000000, backupCount=5, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)

logger.addHandler(handler)


def main() -> None:
    dotenv.load_dotenv()
    # print(os.environ["FSTR_DB_HOST"])
    # print(os.environ["FSTR_DB_PORT"])
    # print(os.environ["FSTR_DB_LOGIN"])
    # print(os.environ["FSTR_DB_PASS"])
    logger.info('Читаем .env')
    try:
        with psycopg2.connect(
            host=os.environ["FSTR_DB_HOST"],
            port=os.environ["FSTR_DB_PORT"],
            user=os.environ["FSTR_DB_LOGIN"],
            password=os.environ["FSTR_DB_PASS"],
            dbname="pereval",
        ) as connection:
            logger.info('Подключение к БД прошло успешно')
            print(connection)
    except psycopg2.OperationalError as e:
        logger.error('Не удалось подключиться к БД')
        print(e)


if __name__ == "__main__":
    main()
