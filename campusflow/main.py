from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("gemini_key")
if not api_key:
    print("api key not found")
else:
    print("api key found")