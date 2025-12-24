import google.generativeai as genai
import os
import json

print(os.getenv("GOOGLE_API_KEY"))

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
models = genai.list_models()
model = genai.GenerativeModel("gemini-flash-lite-latest")

resp = model.generate_content("Say hello", generation_config={"temperature": 0})
print(resp.text)