# 🎙️ Gappi Radio — Voice Controlled Desktop Assistant

A voice controlled desktop assistant built with Python that can track expenses, save notes, and fetch weather updates.

## ✨ Features
- 🎤 Voice recognition (speak to control)
- 💰 Expense tracking (saved to CSV)
- 📝 Note saving (saved to TXT)
- 🌤️ Live weather updates (OpenWeatherMap API)
- 🔊 Text to speech responses

## 🛠️ Tech Stack
- Python 3.13
- pyttsx3 (Text to Speech)
- SpeechRecognition (Voice Input)
- OpenWeatherMap API (Weather)
- CSV & File Handling (Data Storage)

## 🚀 Setup
1. Clone the repo
   git clone https://github.com/Anmol-Aro-ra/Gappi-Radio.git

2. Install dependencies
   pip install -r requirements.txt

3. Create .env file in root folder
   WEATHER_API_KEY=your_api_key_here

4. Run Gappi
   python main.py

## 🗣️ Voice Commands
| Command | Action |
|---|---|
| "add expense 500 food" | Saves expense |
| "show expense" | Shows all expenses |
| "remember to call mom" | Saves note |
| "show notes" | Shows all notes |
| "weather in Delhi" | Gets weather |
| "bye" | Exits Gappi |

## 📁 Project Structure
gappi-radio/
├── core/
│   ├── speaker.py       # Text to speech
│   ├── listener.py      # Voice input
│   ├── base_skill.py    # Abstract base class
│   └── dispatcher.py    # Command routing
├── skills/
│   ├── expense_skill.py # Expense tracking
│   ├── notes_skill.py   # Note saving
│   └── weather_skill.py # Weather updates
├── main.py
└── requirements.txt
