#Zero shot prompting

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

#Zero shot prompting
system_prompt = "You should only answers coding related questions only. Say sorry if the context is different then this."
user_prompt = "Please write a python code to translate the text to french. The text is: Hello, how are you?"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)