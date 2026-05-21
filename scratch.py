import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Force reloading the specific .env file manually
load_dotenv(dotenv_path=".env")

hf_token = os.environ.get("HF_TOKEN")
print("TOKEN loaded:", "YES" if hf_token else "NO")

llm = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=hf_token,
    model="Qwen/Qwen2.5-72B-Instruct",
    temperature=0.1
)

try:
    response = llm.invoke("Hi")
    print("Response:", response.content)
except Exception as e:
    print("ERROR:", e)
