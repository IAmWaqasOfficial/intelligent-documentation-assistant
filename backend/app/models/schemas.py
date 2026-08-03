from pydantic import BaseModel

class QuestionRequest(BaseModel):
    filename: str
    question: str