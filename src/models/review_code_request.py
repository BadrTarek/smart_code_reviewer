from pydantic import BaseModel


class ReviewCodeRequest(BaseModel):
    old_code: str
    new_code: str