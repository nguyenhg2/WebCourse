from pydantic import BaseModel


class Categories(BaseModel):
    name: str
    