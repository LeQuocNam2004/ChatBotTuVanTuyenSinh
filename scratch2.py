import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
hf_token = os.environ.get("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {hf_token}"
}

response = requests.get("https://router.huggingface.co/v1/models", headers=headers)
if response.status_code == 200:
    models = response.json()
    for m in models.get("data", []):
        if "Qwen" in m["id"] or "qwen" in m["id"].lower():
            print(m["id"])
else:
    print("Failed to get models:", response.text)
