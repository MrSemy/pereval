import dotenv
import os

dotenv.load_dotenv()
DB_HOST = os.environ["FSTR_DB_HOST"]
DB_PORT = os.environ["FSTR_DB_PORT"]
DB_USER = os.environ["FSTR_DB_LOGIN"]
DB_PASS = os.environ["FSTR_DB_PASS"]
DB_NAME = "pereval"

TEST_DB_HOST = os.environ["TEST_FSTR_DB_HOST"]
TEST_DB_PORT = os.environ["TEST_FSTR_DB_PORT"]
TEST_DB_USER = os.environ["TEST_FSTR_DB_LOGIN"]
TEST_DB_PASS = os.environ["TEST_FSTR_DB_PASS"]
TEST_DB_NAME = "pereval_test"
