import os, re
from dotenv import load_dotenv
from pathlib import Path

# Step 0: set up the API keys, and file path.

# Load variables from .env into environment

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Error to test importing in Docker
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set. Pass -e OPENAI_API_KEY=... or use --env-file .env")


def generate_code(model, prompt, out_path):
    script_dir = Path(__file__).parent.resolve()

    # Step 1: generate the code based on the provided prompt
    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful coder."},
            {"role": "user", "content": prompt}
        ],
    )

    # Step 2: Format and save the AI-generated Python code

    fenced_code_string = response.choices[0].message.content

    def remove_fences(code_string):
        match = re.search(r"```(?:\w+)?\n(.*?)```", code_string, re.DOTALL)
        return match.group(1) if match else None

    unfenced_code_string = remove_fences(fenced_code_string)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(unfenced_code_string)