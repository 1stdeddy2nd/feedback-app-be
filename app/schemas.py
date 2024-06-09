from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class FeedbackBase(BaseModel):
    name: str = Field(..., max_length=50, examples=["John Doe"])
    score: int = Field(..., ge=1, le=5, examples=[5])
    description: str = Field(..., max_length=50, examples=["Amazing Experience!"])


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50, examples=["John Doe"])
    score: Optional[int] = Field(None, ge=1, le=5, examples=[5])
    description: Optional[str] = Field(
        None, max_length=50, examples=["Amazing Experience!"]
    )


class Feedback(FeedbackBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
