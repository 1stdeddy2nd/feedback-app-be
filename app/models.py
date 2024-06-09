from sqlalchemy import Column, Integer, String
from .database import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    score = Column(Integer, nullable=False)
    description = Column(String(500), nullable=False)
