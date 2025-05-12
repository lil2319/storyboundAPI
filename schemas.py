from pydantic import BaseModel


class BookRecommendationResponse(BaseModel):
    recommended_isbns: str


class BookRecommendationRequest(BaseModel):
    book_title: str
