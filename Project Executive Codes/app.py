import streamlit as st
from translator import Translator
from config import Config
from typing import Dict, List

# Initialize the translator with PALM API
try:
    translator = Translator()
    # Display model information in sidebar
    model_info = translator.get_model_info()
except Exception as e:
    st.error(f"Failed to initialize PALM API and models: {str(e)}")
    st.info("📖 Please follow the API_SETUP_GUIDE.md to configure your API key")
    st.stop()

def main():
    st.set_page_config(
        page_title=Config.PAGE_TITLE,
        page_icon=Config.PAGE_ICON,
        layout=Config.LAYOUT
    )
    
    st.title("🌍 TransLingua")
    st.markdown("### AI-Powered Multi-Language Translator")
    
    # Initialize session state
    if 'translation_history' not in st.session_state:
        st.session_state.translation_history = []
    if 'travel_history' not in st.session_state:
        st.session_state.travel_history = []
    
    # Create tabs for different functionalities
    tab1, tab2 = st.tabs(["📝 Translation", "✈️ Travel Guide"])
    
    with tab1:
        translation_interface()
    
    with tab2:
        travel_guide_interface()

def translation_interface():
    """Translation interface functionality"""
    # Get language preferences from query params or use defaults
    query_params = st.query_params
    source_lang = query_params.get('source', 'English')
    target_lang = query_params.get('target', 'Spanish')
    
    # Sidebar for language selection and model info
    with st.sidebar:
        st.header("🔧 Settings")
        
        # Display model information
        st.markdown("### 🤖 Model Status")
        st.info(f"**API Status:** {model_info['api_status']}")
        st.info(f"**Translation Model:** {model_info['translation_model']}")
        st.info(f"**Travel Model:** {model_info['travel_model']}")
        
        st.markdown("---")
        
        # Source language selection
        source_lang = st.selectbox(
            "Source Language:",
            options=list(Config.LANGUAGES.keys()),
            index=list(Config.LANGUAGES.keys()).index(source_lang) if source_lang in Config.LANGUAGES else 0,
            key="source_language_widget"
        )
        
        # Target language selection
        target_lang = st.selectbox(
            "Target Language:",
            options=list(Config.LANGUAGES.keys()),
            index=list(Config.LANGUAGES.keys()).index(target_lang) if target_lang in Config.LANGUAGES else 1,
            key="target_language_widget"
        )
        
        # Swap languages button
        if st.button("🔄 Swap Languages"):
            # Update query params to trigger rerun with swapped values
            st.query_params.source = target_lang
            st.query_params.target = source_lang
            st.rerun()
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Input Text")
        
        # Text input area
        input_text = st.text_area(
            "Enter text to translate:",
            height=200,
            key="input_text",
            placeholder="Type or paste your text here..."
        )
        
        # Translate button
        translate_button = st.button("🚀 Translate", type="primary")
        
        # Clear button
        if st.button("🗑️ Clear"):
            st.session_state.input_text = ""
            st.session_state.translated_text = ""
            st.rerun()
    
    with col2:
        st.header("Translated Text")
        
        if translate_button and input_text:
            with st.spinner("Translating..."):
                # Perform translation
                translated_text = translator.translate_text(
                    input_text, 
                    source_lang, 
                    target_lang
                )
                
                # Store in session state
                st.session_state.translated_text = translated_text
                
                # Add to history (limit to max items)
                st.session_state.translation_history.append({
                    "source_lang": source_lang,
                    "target_lang": target_lang,
                    "input_text": input_text,
                    "translated_text": translated_text
                })
                
                # Keep only the most recent translations
                if len(st.session_state.translation_history) > Config.MAX_HISTORY_ITEMS:
                    st.session_state.translation_history = st.session_state.translation_history[-Config.MAX_HISTORY_ITEMS:]
                
                # Display translated text
                st.text_area(
                    "Translation:",
                    value=translated_text,
                    height=200,
                    disabled=True
                )
                
                # Copy to clipboard button
                if st.button("📋 Copy Translation"):
                    st.write("Translation copied to clipboard!")
        
        elif 'translated_text' in st.session_state and st.session_state.translated_text:
            st.text_area(
                "Translation:",
                value=st.session_state.translated_text,
                height=200,
                disabled=True
            )
            
            # Copy to clipboard button
            if st.button("📋 Copy Translation"):
                st.write("Translation copied to clipboard!")
    
    # Translation history
    if st.session_state.translation_history:
        st.header("📚 Translation History")
        
        for i, translation in enumerate(reversed(st.session_state.translation_history[-5:])):
            with st.expander(
                f"{translation['source_lang']} → {translation['target_lang']} | "
                f"{translation['input_text'][:50]}..."
            ):
                st.write("**Original Text:**")
                st.write(translation['input_text'])
                st.write("**Translated Text:**")
                st.write(translation['translated_text'])

def travel_guide_interface():
    """Travel guide generation interface"""
    st.header("✈️ AI Travel Guide Generator")
    st.markdown("Generate personalized travel guides using AI!")
    
    # Input fields for travel guide
    col1, col2 = st.columns([1, 1])
    
    with col1:
        destination = st.text_input(
            "🏝️ Destination:",
            placeholder="e.g., Paris, Tokyo, New York",
            key="destination"
        )
        
        duration = st.text_input(
            "⏰ Duration:",
            placeholder="e.g., 3 days, 1 week, 2 weeks",
            key="duration"
        )
    
    with col2:
        interests = st.text_area(
            "🎯 Interests & Preferences:",
            placeholder="e.g., museums, food, adventure, nightlife, shopping, nature",
            height=100,
            key="interests"
        )
        
        budget = st.text_input(
            "💰 Budget (Optional):",
            placeholder="e.g., $1000, luxury, budget-friendly",
            key="budget"
        )
    
    # Generate button
    if st.button("🗺️ Generate Travel Guide", type="primary"):
        if destination and duration and interests:
            with st.spinner("Generating your personalized travel guide..."):
                travel_guide = translator.generate_travel_guide(
                    destination, duration, interests, budget
                )
                
                # Store in session state
                st.session_state.current_travel_guide = travel_guide
                
                # Add to history
                st.session_state.travel_history.append({
                    "destination": destination,
                    "duration": duration,
                    "interests": interests,
                    "budget": budget,
                    "guide": travel_guide
                })
                
                # Keep only the most recent guides
                if len(st.session_state.travel_history) > 5:
                    st.session_state.travel_history = st.session_state.travel_history[-5:]
        else:
            st.warning("⚠️ Please fill in all required fields (Destination, Duration, and Interests).")
    
    # Display generated travel guide
    if 'current_travel_guide' in st.session_state and st.session_state.current_travel_guide:
        st.markdown("---")
        st.header("📋 Your Generated Travel Guide")
        
        # Display the guide with markdown formatting
        st.markdown(st.session_state.current_travel_guide)
        
        # Copy and download buttons
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("📋 Copy Guide"):
                st.write("Travel guide copied to clipboard!")
        with col2:
            if st.button("💾 Save Guide"):
                st.write("Travel guide saved!")
    
    # Travel guide history
    if st.session_state.travel_history:
        st.markdown("---")
        st.header("📚 Recent Travel Guides")
        
        for i, guide in enumerate(reversed(st.session_state.travel_history)):
            with st.expander(
                f"📍 {guide['destination']} | {guide['duration']}"
            ):
                st.write(f"**Interests:** {guide['interests']}")
                if guide['budget']:
                    st.write(f"**Budget:** {guide['budget']}")
                st.markdown(guide['guide'])

if __name__ == "__main__":
    main()
