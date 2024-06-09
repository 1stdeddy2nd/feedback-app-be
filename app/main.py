from fastapi import Depends, FastAPI, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware

from . import crud, schemas
from .database import get_db

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api")


@router.post("/feedbacks/", response_model=schemas.Feedback, status_code=201)
async def create_feedback(
    feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)
):
    try:
        feedback_result = await crud.create_feedback(db=db, feedback=feedback)
        return feedback_result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/feedbacks/{feedback_id}", response_model=schemas.Feedback)
async def update_feedback(
    feedback_id: int,
    feedback_update: schemas.FeedbackUpdate,
    db: Session = Depends(get_db),
):
    try:
        result = await crud.update_feedback(
            db=db, feedback_id=feedback_id, feedback_update=feedback_update
        )
        return result
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/feedbacks/", response_model=list[schemas.Feedback])
async def get_all_feedback(db: AsyncSession = Depends(get_db)):
    feedbacks_result = await crud.get_all_feedback(db)
    return feedbacks_result


@router.get("/feedbacks/{feedback_id}", response_model=schemas.Feedback)
async def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    db_feedback = await crud.get_feedback(db, feedback_id=feedback_id)
    if db_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return db_feedback


@router.delete("/feedbacks/{feedback_id}", status_code=204)
async def delete_feedback(feedback_id: int, db: AsyncSession = Depends(get_db)):
    try:
        await crud.delete_feedback(db=db, feedback_id=feedback_id)
        return {"message": "Feedback deleted successfully"}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


app.include_router(router)
