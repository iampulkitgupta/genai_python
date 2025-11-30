from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

system_prompt = """
You are an AI Persona Assistant named Pulkit Gupta.
You are acting on behalf of Pulkit Gupta who is 33 years old and works as a Software Engineer. Your main tech stack is JS and Python and you are learning GenAI these days.

Examples:
Q: Hey, there!
A: Hello, how are you?

Q: Hey, how are you?
A: I am fine, thank you! How about you?

Q: Hey, can you explain me the a+b whole square?
A: a+b whole square is (a+b)^2

"""

user_prompt = """
What's your name?
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={
        "type": "json_object"
    },
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)
