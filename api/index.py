from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
import logging
from pathlib import Path

# Setup path for templates and static files
base_path = Path(__file__).parent.parent
os_environ = os.environ.copy()
os_environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY', '')

# Initialize Flask app
app = Flask(__name__, template_folder=str(base_path / 'templates'), static_folder=str(base_path / 'static'))
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Groq client
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
if not GROQ_API_KEY:
    logger.warning("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

# System prompt for the Ayurveda chatbot
AYURVEDA_SYSTEM_PROMPT = """You are an expert Ayurvedic practitioner and nutritional scientist with deep knowledge of:
- Ayurveda principles (Doshas: Vata, Pitta, Kapha)
- Ayurvedic herbs and their medicinal properties
- Nutritional science and healthy eating habits
- Treatment of common diseases using Ayurvedic approaches
- Balance of three doshas for optimal health
- Seasonal eating and lifestyle recommendations
- Yoga and meditation for wellness

Always provide accurate, helpful information about Ayurveda and nutrition. Be compassionate and encourage consulting with professionals for serious health conditions. Keep responses informative, concise, and practical."""

# Conversation history for context
conversation_history = {}


@app.route('/')
def home():
    """Render home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render about page"""
    return render_template('about.html')


@app.route('/benefits')
def benefits():
    """Render benefits page"""
    return render_template('benefits.html')


@app.route('/conditions')
def conditions():
    """Render health conditions page"""
    return render_template('conditions.html')


@app.route('/chat')
def chat():
    """Render chatbot page"""
    return render_template('chatbot.html')


@app.route('/api/chat', methods=['POST'])
def chat_api():
    """Handle chat messages using Groq API"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')

        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400

        if not GROQ_API_KEY or not client:
            return jsonify({'error': 'API key not configured'}), 500

        # Initialize conversation history for this session
        if session_id not in conversation_history:
            conversation_history[session_id] = []

        # Add user message to history
        conversation_history[session_id].append({
            "role": "user",
            "content": user_message
        })

        # Keep only last 10 messages for context (to avoid token limits)
        if len(conversation_history[session_id]) > 20:
            conversation_history[session_id] = conversation_history[session_id][-20:]

        # Call Groq API
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": AYURVEDA_SYSTEM_PROMPT
                }
            ] + conversation_history[session_id],
            temperature=0.7,
            max_tokens=1024,
        )

        assistant_message = response.choices[0].message.content

        # Add assistant response to history
        conversation_history[session_id].append({
            "role": "assistant",
            "content": assistant_message
        })

        return jsonify({
            'response': assistant_message,
            'session_id': session_id
        })

    except Exception as e:
        logger.error(f"Error in chat API: {str(e)}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.route('/api/clear-chat', methods=['POST'])
def clear_chat():
    """Clear conversation history"""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'default')
        
        if session_id in conversation_history:
            conversation_history[session_id] = []
        
        return jsonify({'success': True, 'message': 'Chat cleared'})
    except Exception as e:
        logger.error(f"Error clearing chat: {str(e)}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('base.html'), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    logger.error(f"Server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500


# WSGI handler for Vercel
handler = app


# Export app for Vercel
handler = app
