from fastapi import APIRouter
from app.services.answer_service import get_answer

router = APIRouter()


@router.get("/get-answer/{text}", response_model=str)
def get_answer_endpoint(text: str):
    return get_answer(text)
