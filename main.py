import os
import dotenv


def main() -> None:
    dotenv.load_dotenv()
    print(os.environ["FSTR_DB_HOST"])
    print(os.environ["FSTR_DB_PORT"])
    print(os.environ["FSTR_DB_LOGIN"])
    print(os.environ["FSTR_DB_PASS"])


if __name__ == "__main__":
    main()
