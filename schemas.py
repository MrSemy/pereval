from pydantic import BaseModel


class SubmitData(BaseModel):
    id: int
    status: str
