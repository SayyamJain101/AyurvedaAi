@echo off
REM Ayurveda Website - Quick Start Script for Windows

echo.
echo ================================
echo Ayurveda & Nutrition Website
echo Quick Start Script
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/4] Python found. Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created successfully.
) else (
    echo Virtual environment already exists.
)

echo.
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/4] Installing Python dependencies...
pip install -r requirements.txt

echo.
echo [4/4] Setup complete!
echo.
echo ================================
echo IMPORTANT: Setup Your Groq API Key
echo ================================
echo.
echo 1. Go to https://console.groq.com
echo 2. Sign up for a free account
echo 3. Create an API key in the console
echo 4. Create a .env file in this folder with:
echo    GROQ_API_KEY=your_api_key_here
echo.
echo Copy from .env.example:
echo    - Copy .env.example to .env
echo    - Edit .env and paste your API key
echo.
echo ================================
echo Ready to Run!
echo ================================
echo.
echo To start the website, run:
echo    python app.py
echo.
echo Then open: http://localhost:5000
echo.
pause
