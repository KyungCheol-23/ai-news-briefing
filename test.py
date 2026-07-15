from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


for model in client.models.list():
    print(model.name)
    print(model.supported_actions)
    print("-" * 30)


response = client.models.generate_content(
    model="models/gemini-3.5-flash",
    contents="안녕하세요"
)

print(response.text)