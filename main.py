from book_input import get_similar_books_from_openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["https://storybound.ai"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/RecommendationPage/{query}")
async def recommend_books(query: str):
    isbn_list = get_similar_books_from_openai(query)
    return {"recommended_isbns": isbn_list[:10]}
