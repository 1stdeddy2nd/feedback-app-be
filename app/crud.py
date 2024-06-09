from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


async def get_feedback(db: AsyncSession, feedback_id: int):
    query = select(models.Feedback).where(models.Feedback.id == feedback_id)
    result = await db.execute(query)
    feedback = result.scalar_one_or_none()
    return feedback


async def get_all_feedback(db: AsyncSession):
    results = await db.execute(select(models.Feedback))
    feedbacks = results.scalars().all()
    return feedbacks


async def create_feedback(
    db: AsyncSession, feedback: schemas.FeedbackCreate
) -> models.Feedback:
    db_feedback = models.Feedback(
        name=feedback.name, score=feedback.score, description=feedback.description
    )
    db.add(db_feedback)
    await db.commit()
    await db.refresh(db_feedback)
    return db_feedback


async def update_feedback(
    db: AsyncSession, feedback_id: int, feedback_update: schemas.FeedbackUpdate
) -> models.Feedback:
    db_feedback = await get_feedback(db=db, feedback_id=feedback_id)
    if db_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")

    for key, value in feedback_update.model_dump(exclude_unset=True).items():
        setattr(db_feedback, key, value)

    await db.commit()
    await db.refresh(db_feedback)
    return db_feedback


async def delete_feedback(db: AsyncSession, feedback_id: int):
    db_feedback = await get_feedback(db=db, feedback_id=feedback_id)
    if db_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")

    await db.delete(db_feedback)
    await db.commit()
    return {"message": "Feedback deleted successfully"}
