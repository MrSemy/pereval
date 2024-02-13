import dotenv
import os

dotenv.load_dotenv()
DB_HOST = os.environ["FSTR_DB_HOST"]
DB_PORT = os.environ["FSTR_DB_PORT"]
DB_USER = os.environ["FSTR_DB_LOGIN"]
DB_PASS = os.environ["FSTR_DB_PASS"]
DB_NAME = "pereval"
