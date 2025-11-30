from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# client = OpenAI(
#     api_key=os.getenv("PERPLEXITY_API_KEY"),
#     base_url="https://api.perplexity.ai"
# )

# response = client.chat.completions.create(
#     model="sonar",
#     messages=[
#         {"role": "user", "content": "Hello, how are you?"}
#     ]
# )



print(response.choices[0].message.content)