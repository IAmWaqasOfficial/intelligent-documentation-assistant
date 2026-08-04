import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question: str, context: str):

    prompt = f"""
You are an AI assistant for technical documentation.

Answer the user's question ONLY using the provided context.

If the answer is not found in the context, reply:
"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text



def generate_summary(document_text: str):

    prompt = f"""
You are an AI document analysis assistant.

Analyze the following document and provide:

1. Overview:
Give a short explanation of what this document is about.

2. Key Points:
Provide the most important points in bullet form.

Document:
{document_text}

Summary:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text