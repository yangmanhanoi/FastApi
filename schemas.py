from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    datetime: str

class ShowBlog(Blog):
    class Config:
        from_attributes = True