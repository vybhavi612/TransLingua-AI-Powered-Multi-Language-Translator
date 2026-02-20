import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ API key not found in .env file")
    exit(1)

genai.configure(api_key=api_key)

print("🔍 Checking available models...")
print("=" * 50)

# List all available models
try:
    models = genai.list_models()
    
    print("✅ Available Models:")
    for model in models:
        print(f"  - {model.name}")
        print(f"    Display Name: {model.display_name}")
        print(f"    Description: {model.description}")
        print(f"    Supported Generation Methods: {model.supported_generation_methods}")
        print("-" * 30)
        
except Exception as e:
    print(f"❌ Error listing models: {e}")

print("=" * 50)
print("🔍 Testing common model names...")

# Test common model names
common_models = [
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-pro",
    "gemini-pro-vision",
    "text-bison-001",
    "chat-bison-001"
]

for model_name in common_models:
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello")
        print(f"✅ {model_name} - WORKING")
    except Exception as e:
        print(f"❌ {model_name} - {str(e)}")
