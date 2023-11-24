from fastapi import APIRouter
from app.services.answer_service import *

router = APIRouter()


@router.get("/get-answer-basic/{text}", response_model=str)
def get_answer_endpoint(text: str):
    return get_answer_basic(text)


@router.get("/get-answer-emotional/{text}", response_model=str)
def get_answer_endpoint(text: str):
    return get_answer_emotional(text)