from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    author: str
    rating: Optional[int] = None