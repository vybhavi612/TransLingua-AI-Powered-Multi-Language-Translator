# TransLingua - AI-Powered Multi-Language Translator

A sophisticated multi-language translation application powered by Google's Gemini Pro LLM and built with Streamlit.

## Features

- 🌍 **Multi-Language Support**: Translate between 12+ languages including English, Spanish, French, German, Chinese, Japanese, and more
- 🤖 **AI-Powered**: Utilizes Google's Gemini Pro LLM for accurate, context-aware translations
- 🎨 **Modern UI**: Clean, intuitive interface built with Streamlit
- 📚 **Translation History**: Keep track of your recent translations
- 🔄 **Language Swap**: Easily swap source and target languages
- 📋 **Copy to Clipboard**: Quick copy functionality for translated text

## Supported Languages

- English
- Spanish
- French
- German
- Italian
- Portuguese
- Russian
- Chinese
- Japanese
- Korean
- Arabic
- Hindi

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd multi_lan
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Gemini Pro API key**:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the project root
   - Add your API key: `GOOGLE_API_KEY=your_actual_api_key_here`

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Translate text**:
   - Select source and target languages from the sidebar
   - Enter text in the input area
   - Click "Translate" to get your translation
   - Copy the result or view your translation history

## Project Structure

```
multi_lan/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API key)
└── README.md          # Project documentation
```

## Architecture

The application follows a clean architecture:

1. **Frontend**: Streamlit UI for user interaction
2. **Backend**: Gemini Pro LLM for translation processing
3. **Configuration**: Environment variables for API management

## API Configuration

The application uses Google's Gemini Pro API for translations. To set up:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add the key to your `.env` file

## Deployment

### Local Deployment
```bash
streamlit run app.py
```


## Dependencies

- `streamlit`: Web application framework
- `google-generativeai`: Gemini Pro API client
- `python-dotenv`: Environment variable management
- `langchain`: Language model utilities
- `langchain-google-genai`: LangChain integration for Google models

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue in the repository.
