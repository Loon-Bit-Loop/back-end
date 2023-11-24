from pydantic import BaseModel


class Answer(BaseModel):
    answer_text: str
