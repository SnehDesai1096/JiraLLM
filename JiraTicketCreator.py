import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize model
model = genai.GenerativeModel("gemini-flash-lite-latest")

def read_task_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def generate_description_and_ac(task_text: str) -> dict:
    prompt = f"""
You are a professional product manager.

Given the following short task description, generate:
1. A clear and detailed Description
2. Acceptance Criteria as bullet points

Return ONLY valid JSON in this exact format:
{{
  "description": "string",
  "acceptance_criteria": [
    "string",
    "string"
  ]
}}

Task:
{task_text}
"""

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0,
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)

def main():
    task_text = read_task_file("task.txt")

    result = generate_description_and_ac(task_text)

    print("\nDESCRIPTION\n")
    print(result["description"])

    print("\nACCEPTANCE CRITERIA\n")
    for i, ac in enumerate(result["acceptance_criteria"], 1):
        print(f"{i}. {ac}")

if __name__ == "__main__":
    main()
