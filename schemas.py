from pydantic import BaseModel


class text1(BaseModel):
    prompt: str
class main_city(BaseModel):
    city:str
class search(BaseModel):
    query:str
