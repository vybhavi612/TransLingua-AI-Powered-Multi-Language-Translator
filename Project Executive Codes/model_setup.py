"""
Model Setup and Initialization for TransLingua
This file demonstrates the PALM API setup and model initialization process
"""

import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

def setup_palm_api():
    """
    Setup PALM API with proper configuration
    """
    # Step 1: Load environment variables
    load_dotenv()
    
    # Step 2: Get API key from environment
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        st.error("❌ API key not found! Please set GOOGLE_API_KEY in your .env file")
        st.info("📖 Follow the API_SETUP_GUIDE.md to generate your API key")
        return False
    
    # Step 3: Configure the API key
    try:
        genai.configure(api_key=api_key)
        st.success("✅ PALM API configured successfully!")
        return True
    except Exception as e:
        st.error(f"❌ Failed to configure PALM API: {str(e)}")
        return False

def initialize_models():
    """
    Initialize the pre-trained models as specified
    """
    try:
        # Initialize Gemini Pro for translation
        translation_model = genai.GenerativeModel('gemini-pro')
        
        # Initialize Gemini 1.5 Flash for travel guides
        travel_model = genai.GenerativeModel('gemini-1.5-flash')
        
        return {
            'translation_model': translation_model,
            'travel_model': travel_model
        }
    except Exception as e:
        st.error(f"❌ Failed to initialize models: {str(e)}")
        return None

def test_models(models):
    """
    Test the initialized models with simple prompts
    """
    if not models:
        return False
    
    try:
        # Test translation model
        with st.spinner("Testing translation model..."):
            translation_test = models['translation_model'].generate_content(
                "Translate 'hello' to Spanish"
            )
            st.success("✅ Translation model working!")
            st.info(f"Test result: {translation_test.text}")
        
        # Test travel model
        with st.spinner("Testing travel guide model..."):
            travel_test = models['travel_model'].generate_content(
                "Suggest 3 attractions in Paris"
            )
            st.success("✅ Travel guide model working!")
            st.info(f"Test result: {travel_test.text}")
        
        return True
    except Exception as e:
        st.error(f"❌ Model testing failed: {str(e)}")
        return False

def display_model_info():
    """
    Display information about the initialized models
    """
    st.markdown("## 🤖 Model Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📝 Translation Model")
        st.markdown("**Model:** `gemini-pro`")
        st.markdown("**Purpose:** High-quality text translation")
        st.markdown("**Features:**")
        st.markdown("- Context-aware translation")
        st.markdown("- Multiple language support")
        st.markdown("- High accuracy")
    
    with col2:
        st.markdown("### ✈️ Travel Guide Model")
        st.markdown("**Model:** `gemini-1.5-flash`")
        st.markdown("**Purpose:** Fast content generation")
        st.markdown("**Features:**")
        st.markdown("- Quick response times")
        st.markdown("- Comprehensive travel guides")
        st.markdown("- Structured output")

def main():
    """
    Main function for model setup and testing
    """
    st.set_page_config(
        page_title="Model Setup - TransLingua",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 PALM API & Model Setup")
    st.markdown("### Initialize Pre-trained Models for TransLingua")
    
    # Step 1: Setup API
    st.markdown("---")
    st.markdown("## 🔑 Step 1: API Configuration")
    
    if st.button("🚀 Setup PALM API"):
        if setup_palm_api():
            # Step 2: Initialize Models
            st.markdown("---")
            st.markdown("## 🧠 Step 2: Model Initialization")
            
            models = initialize_models()
            if models:
                st.success("✅ Models initialized successfully!")
                
                # Step 3: Display Model Info
                display_model_info()
                
                # Step 4: Test Models
                st.markdown("---")
                st.markdown("## 🧪 Step 3: Model Testing")
                
                if st.button("🔬 Test Models"):
                    test_models(models)
            else:
                st.error("❌ Failed to initialize models")
    
    # Display setup instructions
    st.markdown("---")
    st.markdown("## 📋 Setup Instructions")
    
    with st.expander("📖 Detailed Setup Guide"):
        st.markdown("""
        ### 1. Generate API Key
        1. Visit: https://developers.generativeai.google/
        2. Click "Get API key in Google AI Studio"
        3. Click "Get API key" from right navigation menu
        4. Click "Create API key"
        5. Copy the API key
        
        ### 2. Configure Environment
        1. Open `.env` file
        2. Replace placeholder with your actual API key:
        ```
        GOOGLE_API_KEY=AIzaSyB5U5-f1edVl99djSKEcqDoFLcXXXXXX
        ```
        
        ### 3. Initialize Models
        The application uses two models:
        - **gemini-pro**: For high-quality translations
        - **gemini-1.5-flash**: For fast travel guide generation
        
        ### 4. Test Configuration
        Click "Setup PALM API" then "Test Models" to verify everything works.
        """)

if __name__ == "__main__":
    main()
