"""
Translation module for TransLingua application
Demonstrates Google GenAI API setup and pre-trained model initialization
"""

import os
import google.genai as genai
from dotenv import load_dotenv
from typing import Dict, List, Optional
from config import Config

class Translator:
    """Translation service using Google GenAI LLM - New API Implementation"""
    
    def __init__(self):
        """Initialize the translator with Google GenAI API and pre-trained models"""
        try:
            # Step 1: Load environment variables
            load_dotenv()
            
            # Step 2: Get API key
            self.api_key = os.getenv("GOOGLE_API_KEY")
            if not self.api_key:
                raise ValueError("GOOGLE_API_KEY not found in environment variables")
            
            # Step 3: Initialize client
            self.client = genai.Client(api_key=self.api_key)
            
            # Step 4: Set model name
            self.model_name = Config.MODEL_NAME
            
            print("✅ Google GenAI API configured successfully")
            print("✅ Pre-trained models initialized:")
            print(f"   - Translation model: {Config.MODEL_NAME}")
            print(f"   - Travel guide model: {Config.MODEL_NAME}")
            
        except Exception as e:
            raise Exception(f"Failed to initialize Google GenAI API and models: {str(e)}")
    
    def get_model_info(self) -> Dict[str, str]:
        """
        Get information about initialized models
        """
        return {
            "api_status": "configured" if self.api_key else "not configured",
            "translation_model": Config.MODEL_NAME,
            "travel_model": Config.MODEL_NAME,
            "api_key_prefix": self.api_key[:10] + "..." if self.api_key else "None"
        }
    
    def translate_text(
        self, 
        text: str, 
        source_lang: str, 
        target_lang: str,
        context: Optional[str] = None
    ) -> str:
        """
        Translate text using Google GenAI LLM
        
        Args:
            text: Text to translate
            source_lang: Source language name
            target_lang: Target language name
            context: Optional context for better translation
            
        Returns:
            Translated text
        """
        if not text.strip():
            return ""
        
        # Build translation prompt
        base_prompt = f"""
        Translate the following text from {source_lang} to {target_lang}.
        Provide only the translation without any additional explanations or formatting.
        Maintain the original tone, style, and context of the text.
        
        Text to translate: {text}
        
        Translation:
        """
        
        if context:
            base_prompt = f"""
            Translate the following text from {source_lang} to {target_lang}.
            Context: {context}
            Provide only the translation without any additional explanations or formatting.
            Maintain the original tone, style, and context of the text.
            
            Text to translate: {text}
            
            Translation:
            """
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=base_prompt
            )
            return response.text.strip()
        except Exception as e:
            return f"Translation Error: {str(e)}"
    
    def generate_travel_guide(self, destination: str, duration: str, interests: str, budget: str = "") -> str:
        """
        Generate a comprehensive travel guide using Google GenAI
        
        Args:
            destination: Travel destination
            duration: Duration of travel (e.g., "3 days", "1 week")
            interests: Travel interests and preferences
            budget: Optional budget information
            
        Returns:
            Generated travel guide
        """
        prompt = f"""
        Create a comprehensive travel guide for {destination} for a {duration} trip.
        
        Traveler's interests: {interests}
        {f'Budget: {budget}' if budget else ''}
        
        Please provide:
        1. Best time to visit
        2. Top attractions and activities
        3. Recommended itinerary day by day
        4. Local cuisine recommendations
        5. Transportation tips
        6. Accommodation suggestions
        7. Cultural tips and etiquette
        8. Packing recommendations
        
        Format the response in a clear, organized manner with headings and bullet points.
        """
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            return f"Travel Guide Generation Error: {str(e)}"
    
    def detect_language(self, text: str) -> str:
        """
        Detect the language of the given text
        
        Args:
            text: Text to analyze
            
        Returns:
            Detected language name
        """
        prompt = f"""
        Detect the language of the following text. 
        Respond with only the language name in English (e.g., "English", "Spanish", "French").
        
        Text: {text}
        
        Language:
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Detection Error: {str(e)}"
    
    def get_supported_languages(self) -> Dict[str, str]:
        """
        Get list of supported languages
        
        Returns:
            Dictionary of language names and codes
        """
        return Config.LANGUAGES
    
    def refine_translation(
        self, 
        original_text: str, 
        translated_text: str, 
        feedback: str
    ) -> str:
        """
        Refine translation based on user feedback
        
        Args:
            original_text: Original text
            translated_text: Current translation
            feedback: User feedback for improvement
            
        Returns:
            Refined translation
        """
        prompt = f"""
        Refine the following translation based on the provided feedback.
        
        Original text: {original_text}
        Current translation: {translated_text}
        Feedback: {feedback}
        
        Provide only the refined translation:
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Refinement Error: {str(e)}"
