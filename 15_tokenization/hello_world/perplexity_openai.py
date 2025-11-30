from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    base_url="https://api.perplexity.ai"
)

system_prompt = "You are an expert in Maths and only answers maths questions"
user_prompt = "Explain me statisitcs topics in few words?"

response = client.chat.completions.create(
    model="sonar",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)