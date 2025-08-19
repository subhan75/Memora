# 🧠Memora -  Memory-Powered Personal Assistant

A sophisticated AI-powered chatbot that combines conversational memory, voice interaction, and sentiment analysis to provide a personalized mental health support experience.

## 🌟 Features

### 🤖 **AI-Powered Conversations**
- **GPT-4 Integration**: Powered by OpenAI's latest language model for intelligent, contextual responses
- **Memory System**: Remembers past conversations and provides personalized responses based on user history
- **Contextual Understanding**: Maintains conversation context across sessions

### 🎤 **Voice Interaction**
- **Speech-to-Text**: Real-time audio transcription using OpenAI Whisper
- **Voice Input**: Speak naturally to interact with the assistant
- **Multi-modal Communication**: Seamlessly switch between text and voice

### 📊 **Sentiment Analysis**
- **Real-time Analysis**: Analyzes the emotional tone of user messages
- **Mood Tracking**: Provides insights into conversation sentiment
- **Emotional Intelligence**: Adapts responses based on detected emotions

### 💾 **Memory Management**
- **Persistent Memory**: Stores conversation history using Mem0 AI
- **User-specific Context**: Each user has their own memory space
- **Relevant Recall**: Retrieves contextually relevant past conversations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Mem0 AI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Mental_Health_Chatbot/Memora
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   MEM0_API_KEY=your_mem0_api_key_here
   ```

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

## 🏗️ Architecture

### Core Components

#### `core.py` - Main Assistant Logic
```python
class MemoryAssistant:
    def __init__(self, user_id="default_user")
    def ask(self, query: str) -> str
    def transcribe_audio(self, audio_data: bytes) -> str
    def analyze_sentiment(self, text: str) -> str
```

**Key Methods:**
- **`ask()`**: Processes text queries with memory context
- **`transcribe_audio()`**: Converts speech to text using Whisper
- **`analyze_sentiment()`**: Analyzes emotional tone using TextBlob

#### `app.py` - Streamlit Interface
- **Chat Interface**: Real-time messaging with the assistant
- **Voice Input**: Audio recording and transcription
- **Session Management**: Maintains conversation state
- **Error Handling**: Graceful error recovery

### Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Model** | OpenAI GPT-4 | Natural language processing |
| **Memory** | Mem0 AI | Conversation memory storage |
| **Speech Recognition** | OpenAI Whisper | Audio transcription |
| **Sentiment Analysis** | TextBlob | Emotional tone detection |
| **Web Interface** | Streamlit | User interface |
| **Environment** | Python venv | Dependency isolation |

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 access | ✅ |
| `MEM0_API_KEY` | Mem0 AI key for memory storage | ✅ |

### User Settings

- **User ID**: Customizable identifier for memory isolation
- **Memory Limit**: Configurable number of past conversations to recall
- **Sentiment Display**: Toggle sentiment analysis visibility

## 📱 Usage Guide

### Text Chat
1. Type your message in the chat input
2. Press Enter or click Send
3. The assistant responds with context from your conversation history

### Voice Interaction
1. Click the microphone icon
2. Speak your message clearly
3. The system transcribes and processes your speech
4. Receive a text response from the assistant

### Memory Features
- **Automatic Memory**: Conversations are automatically saved
- **Contextual Recall**: Relevant past conversations are retrieved
- **User Isolation**: Each user ID has separate memory space

### Sentiment Analysis
- **Real-time Display**: Current message sentiment shown in sidebar
- **Emotional Tracking**: Monitor conversation tone over time
- **Adaptive Responses**: Assistant adjusts based on detected emotions

## 🛠️ Development

### Project Structure
```
Memora/
├── app.py              # Streamlit application
├── core.py             # Core assistant logic
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── .env               # Environment variables (create this)
└── venv/              # Virtual environment
```

### Adding New Features

#### Custom Sentiment Analysis
```python
def custom_sentiment_analyzer(self, text: str) -> dict:
    # Implement custom sentiment logic
    return {
        "sentiment": "positive",
        "confidence": 0.85,
        "emotions": ["joy", "excitement"]
    }
```

#### Extended Memory Features
```python
def get_memory_summary(self, user_id: str) -> str:
    # Retrieve memory summary for user
    memories = memory.search(query="", user_id=user_id, limit=10)
    return self.summarize_memories(memories)
```

### Testing
```bash
# Run the application
streamlit run app.py

# Test specific components
python -c "from core import MemoryAssistant; print('Core module works!')"
```

## 🔒 Security & Privacy

### Data Protection
- **Local Processing**: Audio transcription happens locally
- **Secure Storage**: Memory data stored securely via Mem0 AI
- **User Isolation**: Complete separation between user sessions
- **No Data Retention**: No permanent storage of sensitive conversations

### API Security
- **Environment Variables**: API keys stored securely
- **No Hardcoding**: Sensitive data never committed to code
- **Access Control**: User-specific memory isolation

## 🚨 Troubleshooting

### Common Issues

#### Import Errors
```bash
# Ensure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

#### API Key Issues
```bash
# Check environment variables
echo $OPENAI_API_KEY
echo $MEM0_API_KEY

# Verify .env file exists and contains keys
cat .env
```

#### Memory Issues
- **Clear Browser Cache**: Refresh the Streamlit app
- **Reset Session**: Use a new User ID
- **Check API Limits**: Verify Mem0 AI quota

#### Audio Problems
- **Microphone Permissions**: Allow browser microphone access
- **Audio Quality**: Ensure clear speech and minimal background noise
- **Network Connection**: Stable internet required for transcription

### Error Messages

| Error | Solution |
|-------|----------|
| `No module named 'whisper'` | Install openai-whisper: `pip install openai-whisper` |
| `API key not found` | Check .env file and environment variables |
| `Memory operation failed` | Verify Mem0 AI API key and network connection |
| `Audio transcription failed` | Check microphone permissions and audio quality |

## 📈 Performance Optimization

### Memory Management
- **Efficient Queries**: Limit memory searches to relevant context
- **Batch Operations**: Group memory operations when possible
- **Cache Management**: Implement response caching for common queries

### Response Time
- **Async Processing**: Use asynchronous operations for API calls
- **Connection Pooling**: Reuse HTTP connections
- **Request Batching**: Combine multiple API requests

## 🔮 Future Enhancements

### Planned Features
- [ ] **Multi-language Support**: Internationalization for global users
- [ ] **Advanced Analytics**: Detailed conversation insights and trends
- [ ] **Integration APIs**: Connect with external mental health services
- [ ] **Mobile App**: Native iOS and Android applications
- [ ] **Group Sessions**: Multi-user conversation support
- [ ] **Custom Models**: Fine-tuned models for specific use cases

### Technical Improvements
- [ ] **WebSocket Support**: Real-time bidirectional communication
- [ ] **Database Integration**: Persistent storage for analytics
- [ ] **Microservices**: Scalable architecture for production
- [ ] **Docker Support**: Containerized deployment
- [ ] **CI/CD Pipeline**: Automated testing and deployment

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with detailed description

### Code Standards
- **Python**: Follow PEP 8 style guidelines
- **Documentation**: Add docstrings to all functions
- **Testing**: Include unit tests for new features
- **Error Handling**: Implement comprehensive error handling

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI**: For GPT-4 and Whisper APIs
- **Mem0 AI**: For memory management capabilities
- **Streamlit**: For the web interface framework
- **TextBlob**: For sentiment analysis functionality

## 📞 Support

### Getting Help
- **Documentation**: Check this README for common solutions
- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Join community discussions for feature requests

### Contact Information
- **Email**: [your-email@example.com]
- **GitHub**: [your-github-profile]
- **LinkedIn**: [your-linkedin-profile]

---

**⚠️ Important Notice**: This application is designed for general conversation and support. It is not a substitute for professional mental health care. If you're experiencing a mental health crisis, please contact a mental health professional or emergency services immediately.

**Made with ❤️ for better mental health support**
