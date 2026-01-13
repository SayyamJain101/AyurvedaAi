# Ayurveda and Nutritional Science Website

A minimalistic yet powerful website dedicated to Ayurveda and Nutritional Science with an intelligent chatbot powered by Groq API.

## Features

- **Historical Indian Template**: Showcasing Ayurveda and its benefits with a minimalistic design
- **Intelligent Chatbot**: Powered by Groq API to answer questions about Ayurveda, diseases, and wellness
- **Responsive Design**: Beautiful and intuitive user interface
- **Knowledge Base**: Comprehensive information about Ayurvedic principles and nutritional science

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Groq API Key (get it from https://console.groq.com)

### Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

### Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
ayurveda-website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not included in git)
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── script.js     # Frontend JavaScript
└── templates/
    ├── base.html        # Base template
    ├── index.html       # Home page
    ├── about.html       # About Ayurveda
    ├── benefits.html    # Ayurveda Benefits
    ├── chatbot.html     # Chatbot interface
    └── conditions.html  # Health Conditions
```

## API Endpoints

- `GET /` - Home page
- `GET /about` - About Ayurveda
- `GET /benefits` - Benefits page
- `GET /conditions` - Health conditions
- `GET /chat` - Chat interface
- `POST /api/chat` - Chat endpoint (accepts JSON with 'message' field)

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI**: Groq API
- **Styling**: Custom CSS with Indian design inspiration
