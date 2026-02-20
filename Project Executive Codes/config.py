"""
Configuration file for TransLingua application
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration class"""
    
    # API Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # Model Configuration
    MODEL_NAME = "gemini-2.5-flash"
    TEMPERATURE = 0.7
    MAX_OUTPUT_TOKENS = 2048
    
    # UI Configuration
    PAGE_TITLE = "TransLingua - AI-Powered Multi-Language Translator"
    PAGE_ICON = "🌍"
    LAYOUT = "wide"
    
    # Supported Languages
    LANGUAGES = {
        "English": "en",
        "Spanish": "es", 
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt",
        "Russian": "ru",
        "Chinese": "zh",
        "Japanese": "ja",
        "Korean": "ko",
        "Arabic": "ar",
        "Hindi": "hi",
        "Dutch": "nl",
        "Swedish": "sv",
        "Norwegian": "no",
        "Danish": "da",
        "Finnish": "fi",
        "Polish": "pl",
        "Turkish": "tr",
        "Greek": "el"
    }
    
    # Translation History
    MAX_HISTORY_ITEMS = 10
    
    @classmethod
    def validate_config(cls):
        """Validate configuration settings"""
        if not cls.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        return True
