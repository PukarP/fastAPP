from pydantic import BaseModel

class CreatePost(BaseModel):
    title: str
    content: str
    author: str
