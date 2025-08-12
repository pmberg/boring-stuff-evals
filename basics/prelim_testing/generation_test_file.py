import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

#Error to test importing in Docker
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set. Pass -e OPENAI_API_KEY=... or use --env-file .env")


# Use it with the OpenAI API client
from openai import OpenAI
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4o", "gpt-3.5-turbo", etc.
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Give the solution to the equation 2+2. Answer as a single numeral with no clarification."}
    ],
)

print(response.choices[0].message.content)
