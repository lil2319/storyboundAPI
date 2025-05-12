from typing import List
from openai import OpenAI
import json

client = OpenAI()

instructions = (
    "You are an expert literary analyst and book recommender. "
    "Given a single book title, your task is to return 10 book recommendations that closely match the original "
    "in terms of themes, tone, genre, and emotional impact. Each recommendation must be thoughtfully selected "
    "based on deep understanding of the original book’s content. We want to give unique recommendations\n\n"
    'Respond with a JSON object containing a single key: "recommendations", which is a list of 10 ISBNs '
    "(preferably ISBN-13) representing your recommended books. Do not include any explanations or book titles—just the JSON response.\n\n"
    "Example input:\n"
    '"From Blood and Ash"\n\n'
    "Expected output format:\n"
    "{\n"
    '  "recommendations": [\n'
    '    "9781250238795",\n'
    '    "9781682815885",\n'
    '    "9781250750112",\n'
    '    "9780349420880",\n'
    '    "9780349420897",\n'
    '    "9780349420897",\n'
    '    "9781250196231",\n'
    '    "9780062678416",\n'
    '    "9780553573404",\n'
    '    "9780345538374"\n'
    "  ]\n"
    "}"
)


def get_similar_books_from_openai(
    book_title: str,
) -> List[str]:
    response = client.responses.create(
        model="gpt-4.1", instructions=instructions, input=book_title
    )
    text_json = response.output[0].content[0].text
    recommendations = json.loads(text_json)["recommendations"]
    print(recommendations)
    return recommendations
