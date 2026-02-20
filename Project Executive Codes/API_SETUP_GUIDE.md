# PALM API Setup Guide

## Step 1: Generate PALM API Key

1. **Visit Google AI Studio**
   - Go to: https://developers.generativeai.google/
   - Click on "Get API key in Google AI Studio"

2. **Create API Key**
   - Click on "Get API key" from the right navigation menu
   - Click on "Create API key"
   - Copy the generated API key (it will look like: `AIzaSyB5U5-f1edVl99djSKEcqDoFLcXXXXXX`)

## Step 2: Update Environment Variables

Add your API key to the `.env` file:

```bash
GOOGLE_API_KEY=AIzaSyB5U5-f1edVl99djSKEcqDoFLcXXXXXX
```

## Step 3: Model Initialization

The application is already configured to use the correct models:

### Translation Model (Gemini Pro)
- Model: `gemini-pro`
- Purpose: High-quality text translation
- Configuration: Temperature 0.7, Max tokens 2048

### Travel Guide Model (Gemini 1.5 Flash)
- Model: `gemini-1.5-flash`
- Purpose: Fast content generation for travel guides
- Configuration: Optimized for quick responses

## Step 4: Import Configuration

The necessary imports are already configured in the application:

```python
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
```

## Step 5: API Configuration

The API is configured in the `translator.py` file:

```python
# Load environment variables
load_dotenv()

# Configure Gemini Pro API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize models
model = genai.GenerativeModel('gemini-pro')  # For translation
travel_model = genai.GenerativeModel('gemini-1.5-flash')  # For travel guides
```

## Step 6: Verification

To verify your setup:

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   streamlit run app.py
   ```

3. **Test functionality**:
   - Try translating text in the Translation tab
   - Try generating a travel guide in the Travel Guide tab

## Troubleshooting

### API Key Issues
- **Error**: "API key not valid"
- **Solution**: Ensure you've copied the complete API key without extra spaces

### Model Access Issues
- **Error**: "Model not found"
- **Solution**: Ensure you have access to the specified models in your Google Cloud project

### Import Issues
- **Error**: "Module not found"
- **Solution**: Install all required dependencies from requirements.txt

## API Key Security

- Never commit your `.env` file to version control
- Keep your API key secure and private
- Use environment variables for deployment
- Consider using API key rotation for production applications

## Next Steps

Once your API key is set up:
1. Update the `.env` file with your actual API key
2. Restart the Streamlit application
3. Test both translation and travel guide features
4. Deploy your application when ready
