from typing import List
from openai import OpenAI
import json

client = OpenAI()

instructions = (
    "You are an expert in books of all genres and themes. When given a book title, "
    "return a list of 10 book recommendations that are similar in theme, tone, or genre. "
    "Only include books that are distinct from the original and from each other — no duplicates. "
    "Return the output strictly as a JSON object with a single key 'recommendations' whose value is "
    "a list of 10 ISBN-13 numbers of the recommended books.\n\n"
    "Example input:\n"
    '"A Court of Thorns and Roses"\n\n'
    "Example output:\n"
    "{\n"
    '  "recommendations": [\n'
    '    "9781619630345",\n'
    '    "9781649374042",\n'
    '    "9781952457005",\n'
    '    "9780062878021",\n'
    '    "9780316310277",\n'
    '    "9781635574043",\n'
    '    "9781595148049",\n'
    '    "9781250268396",\n'
    '    "9780008609199",\n'
    '    "9781250189967"\n'
    "  ]\n"
    "}\n\n"
    "Do not include any additional explanation or commentary — just return the JSON object."
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
