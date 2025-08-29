import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY is not set")

# OpenRouter API endpoint
url = "https://openrouter.ai/api/v1/chat/completions"

# Request payload
payload = {
    "model": "openai/gpt-oss-20b:free",
    "messages": [
        {"role": "system", "content": "You are Writer agent, generate stories,poems,essay etc."},
        {"role": "user", "name": "Writer", "content": "write a short essay on independence day in good simple english."}
    ]
}

# Request headers
headers = {
    "Authorization": f"Bearer {openrouter_api_key}",
    "Content-Type": "application/json"
}

# Send request
response = requests.post(url, headers=headers, json=payload)

# Parse response
if response.status_code == 200:
    data = response.json()
    print(data["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)
