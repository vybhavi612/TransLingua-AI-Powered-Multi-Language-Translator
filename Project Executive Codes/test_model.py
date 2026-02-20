import os
import google.genai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

print("Testing with gemini-2.5-flash...")

# Test with the new API
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello, translate 'hello world' to Spanish"
    )
    print("✅ Model works!")
    print("Response:", response.text)
except Exception as e:
    print("❌ Model failed:", e)
