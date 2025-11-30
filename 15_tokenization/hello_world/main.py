from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-5-nano",
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