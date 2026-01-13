# Ayurveda Website - Setup & Installation Guide

## 🚀 Quick Start

### Step 1: Get Groq API Key

1. Go to https://console.groq.com
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the API key (you'll need it in Step 3)

### Step 2: Install Python Dependencies

**Windows (Command Prompt or PowerShell):**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**macOS/Linux:**

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

1. Create a `.env` file in the root directory (copy from `.env.example`)
2. Add your Groq API key:

```
GROQ_API_KEY=your_actual_api_key_here
```

### Step 4: Run the Application

```bash
# Make sure your virtual environment is activated
python app.py
```

The application will start at: **http://localhost:5000**

## 📁 Project Structure

```
ayurveda-website/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── .env.example               # Template for .env file
├── README.md                  # Project documentation
├── SETUP_GUIDE.md            # This file
│
├── static/                    # Static files
│   ├── css/
│   │   └── style.css         # Minimalistic Indian design styling
│   └── js/
│       └── script.js         # Chatbot frontend logic
│
└── templates/                # HTML templates
    ├── base.html            # Base template with header/footer
    ├── index.html           # Home page
    ├── about.html           # About Ayurveda
    ├── benefits.html        # Health benefits
    ├── conditions.html      # Health conditions & treatments
    └── chatbot.html         # Chatbot interface
```

## 🌍 Accessing the Website

Once running, navigate to:

- **Home:** http://localhost:5000/
- **About Ayurveda:** http://localhost:5000/about
- **Benefits:** http://localhost:5000/benefits
- **Health Conditions:** http://localhost:5000/conditions
- **AI Chat:** http://localhost:5000/chat

## 🤖 Using the Chatbot

The chatbot is powered by Groq's Mixtral 8x7B model and understands:

- Ayurvedic principles (doshas, agni, ama)
- Herbs and their medicinal properties
- Nutritional science and healthy eating
- Treatment of various health conditions
- Lifestyle and wellness practices
- Seasonal eating and routines

### Example Questions:

- "What is Pitta dosha?"
- "How can I improve my digestion?"
- "What herbs help with anxiety?"
- "How to do oil massage (Abhyanga)?"
- "Is turmeric good for inflammation?"

## 🔧 Troubleshooting

### "Module not found" error

```bash
# Make sure virtual environment is activated and run:
pip install -r requirements.txt
```

### "GROQ_API_KEY not found" error

1. Check that `.env` file exists in the root directory
2. Verify the API key is correctly copied
3. Make sure there's no extra whitespace in the `.env` file

### Port 5000 already in use

Edit `app.py` and change the port:

```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change to 5001 or another port
```

### Chatbot not responding

1. Verify your Groq API key is valid (not expired/revoked)
2. Check internet connection
3. Check that Groq service is operational

## 🎨 Customization

### Change Colors

Edit `static/css/style.css` - Look for `:root` CSS variables:

```css
--primary-color: #8b4513; /* Change this */
--secondary-color: #daa520; /* And this */
```

### Change Website Content

- Edit HTML files in `templates/` folder
- Update text, add new sections, modify structure

### Modify Chatbot Behavior

In `app.py`, edit the `AYURVEDA_SYSTEM_PROMPT` to change chatbot personality or knowledge focus.

## 📊 API Endpoints

| Method | Endpoint        | Description                                                 |
| ------ | --------------- | ----------------------------------------------------------- |
| GET    | /               | Home page                                                   |
| GET    | /about          | About Ayurveda page                                         |
| GET    | /benefits       | Benefits page                                               |
| GET    | /conditions     | Health conditions page                                      |
| GET    | /chat           | Chatbot interface                                           |
| POST   | /api/chat       | Chat endpoint (JSON: `{message: "...", session_id: "..."}`) |
| POST   | /api/clear-chat | Clear chat history (JSON: `{session_id: "..."}`)            |

## 🔒 Security Notes

1. Never commit `.env` file to version control
2. Keep API keys private
3. The chatbot doesn't store conversations after clearing
4. For production, consider:
   - Using environment variables instead of `.env`
   - Adding authentication
   - Implementing rate limiting
   - Using HTTPS

## 📈 Performance Tips

1. The chatbot uses context history (last 20 messages) for responses
2. Adjust token limits if responses are too long/short
3. Different Groq models can be used for speed/quality trade-off

## 🆘 Support

For issues with:

- **Groq API:** https://console.groq.com/docs
- **Flask:** https://flask.palletsprojects.com/
- **Python:** https://www.python.org/

## 📝 Notes

- The website is fully functional with historical Indian design
- The chatbot uses Groq's Mixtral model for intelligent responses
- Everything is built in Python as requested
- No databases required - stateless design

## 🎯 Next Steps

1. Customize colors and fonts to match your branding
2. Add your own Ayurvedic content
3. Integrate with other services as needed
4. Deploy to a hosting service (Heroku, PythonAnywhere, AWS, etc.)

Enjoy your Ayurveda website! 🙏
