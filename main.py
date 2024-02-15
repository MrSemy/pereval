
from fastapi import FastAPI
import router


app = FastAPI(
    title="pereval",
    version="1.0.0",
    description="pereval",
)


def main() -> None:
    pass


app.include_router(
    router.router,
)


if __name__ == "__main__":
    main()
