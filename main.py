from fastapi import FastAPI

from app.api.endpoints import answer
from app.models.answer_model import Answer

app = FastAPI()

app.include_router(answer.router, prefix="/api", tags=["answer"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
