# 🤖 Groq Chatbot

A simple and elegant chatbot built using Streamlit and Groq's API, powered by the Llama 3.1 model.

## 🌟 Features

- **Real-time Chat**: Interactive chat interface with message history
- **Groq AI Integration**: Powered by Groq's fast inference API
- **Multiple Model Support**: Easy to switch between different AI models
- **Clean UI**: Built with Streamlit for a responsive web interface
- **Session Memory**: Maintains conversation context throughout the session

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Groq API Key (get it from [Groq Console](https://console.groq.com/))

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd yyy
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**
   - The project includes a `.env` file with your API key
   - **For security**: Replace the API key in `.env` with your actual key from [Groq Console](https://console.groq.com/)
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```
   - **Important**: Never commit your actual API key to version control!

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - Start chatting with the AI!

## 📁 Project Structure

```
yyy/
├── app.py              # Main Streamlit application
├── chat.py             # Additional chat functionality (if any)
├── gemma_chatbot.py    # Gemma model chatbot variant
├── mixtral_chatbot.py  # Mixtral model chatbot variant
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API keys)
├── .gitignore         # Git ignore file
└── README.md          # Project documentation
```

## 🛠️ Configuration

### Supported Models

The app currently uses `llama-3.1-8b-instant`, but you can easily switch to other Groq models:

- `llama-3.1-8b-instant` - Fast and efficient (current)
- `llama-3.1-70b-versatile` - More powerful, slower
- `mixtral-8x7b-32768` - Good for longer conversations
- `gemma2-9b-it` - Google's Gemma model

To change the model, update line 32 in `app.py`:
```python
"model": "your_preferred_model_here",
```

### Customization

You can customize various aspects:

- **Temperature**: Adjust creativity (0.0 - 2.0) in line 35
- **Page Title**: Change in line 8
- **UI Theme**: Modify Streamlit configuration

## 🔧 Troubleshooting

### Common Issues

1. **Model Decommissioned Error**
   - Solution: Update to a supported model (already fixed in current version)

2. **API Key Issues**
   - Ensure your API key is valid and has sufficient credits
   - Check [Groq Console](https://console.groq.com/) for key status

3. **Installation Problems**
   - Make sure you have Python 3.7+
   - Try: `pip install --upgrade pip` before installing requirements

### Error Messages

- **400 Error**: Usually indicates API key issues or invalid model
- **429 Error**: Rate limit exceeded, wait and retry
- **500 Error**: Server-side issue, try again later

## 📋 Requirements

The `requirements.txt` includes:
- `streamlit` - Web app framework
- `requests` - HTTP library for API calls
- `python-dotenv` - Load environment variables from .env file

## 🤝 Contributing

Feel free to contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Links

- [Groq Documentation](https://console.groq.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq Model Deprecations](https://console.groq.com/docs/deprecations)

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Review Groq's documentation
3. Open an issue in this repository

---

**Happy Chatting! 🎉**