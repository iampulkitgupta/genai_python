#Few shot prompting

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

#Few shot prompting
system_prompt = """
You should only answers coding related questions only. Say sorry if the context is different then this.

Rule:
-Strictly follow the output in JSON format

Output Format:
{
    "answer": "Answer"
}

Examples:
Q: Can you explain the a+b whole square?
A: {{"answer": "Sorry, I can only answer coding related questions."}}

Q: Hey, write a code in python for adding two numbers.
A: {{"answer": "def add(a+b):\n    return a+b"}}
"""
user_prompt = "Write me a code for adding two number in js"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)
# 1. Few Shot Prompting: The model is able to understand the context and able to answer the question based on the examples given to it. 
