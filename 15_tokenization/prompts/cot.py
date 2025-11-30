# Chain of Thoughts Prompting

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

system_prompt = """
    You are an expert AI assistant in resolving user queries using chain of thoughts
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you have planned, you need to execute the plan step by step.

    Rules:
    - Strictly follow the output in JSON format
    - Do not include any extra text in the output
    - Only run one step at a time.
    - The Sequence of steps is: START, PLAN, OUTPUT

    Examples:
    Q: Can you explain the a+b whole square?
    A: {"START": "a+b whole square is (a+b)^2", "PLAN": "(a+b)^2 = a^2 + 2ab + b^2", "OUTPUT": "a+b whole square is (a+b)^2"}

    Q: Hey, write a code in python for adding two numbers.
    A: {"START": "I need to write a code in python for adding two numbers", "PLAN": "I need to write a code in python for adding two numbers", "OUTPUT": "def add(a,b):\n    return a+b"}       

"""

user_prompt = "Hey, write a code in python for adding two numbers."

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