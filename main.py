from fastapi import FastAPI
from router import pereval_router, submitdata_router


app = FastAPI(
    title="pereval",
    version="1.0.0",
    description="pereval",
    openapi_tags=[
        {
            "name": "API для получения, добавления и редактирования данных о перевалах",
            "description": "С помощью данных API Вы сможете получить, добавить и редактировать данные о перевалах. ",
        }
    ]
)


def main() -> None:
    pass


app.include_router(
    router=pereval_router,
)

app.include_router(
    router=submitdata_router,
)

if __name__ == "__main__":
    main()
