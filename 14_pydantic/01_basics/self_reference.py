from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Comment(BaseModel):
    id: int
    text: str
    author: str
    created_at: datetime
    comment: Optional[List['Comment']] = None

Comment.model_rebuild()

comment = Comment(id=1, text="First comment", author="John Doe", created_at=datetime.now(), comment=[Comment(id=2, text="Second comment", author="John Doe", created_at=datetime.now(), comment=None)])

print(comment)