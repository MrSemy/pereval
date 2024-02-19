from pydantic import BaseModel


class SubmitData(BaseModel):
    id: int
    status: str


class PerevalAdded(BaseModel):
    id: int
    title: str
    beauty_title: str
    other_titles: str
    connect: str
    level_winter: str
    level_summer: str
    level_autumn: str
    level_spring: str
    status: str

class AddPereval(BaseModel):
    title: str
    beauty_title: str
    other_titles: str
    connect: str
    level_winter: str
    level_summer: str
    level_autumn: str
    level_spring: str
    status: str
