import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from core.base_skill import BaseSkill


class WeatherSkill(BaseSkill):

    def __init__(self, speaker):
        env_path = Path(__file__).parent.parent / '.env'
        load_dotenv(dotenv_path=env_path)
        self.speaker = speaker
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        

    def get_keywords(self):
        return ["weather", "temperature", "forecast", "मौसम"]

    def handle(self, command: str):
        city = self.extract_city(command)
        self.get_weather(city)

    def extract_city(self, command: str):
        trigger_words = ["weather in", "temperature in",
                         "forecast in", "मौसम in"]
        for trigger in trigger_words:
            if trigger in command:
                return command.split(trigger, 1)[-1].strip()
        return command.split()[-1].strip()

    def get_weather(self, city: str):
        if not city:
            self.speaker.say("Please tell me which city")
            return
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            print(f"API response code: {data.get('cod')}")
            if data.get("cod") != 200:
                self.speaker.say(f"Could not find weather for {city}")
                return
            temp        = data["main"]["temp"]
            feels_like  = data["main"]["feels_like"]
            humidity    = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            result = (f"Weather in {city} is {description}. "
                      f"Temperature is {temp} degrees. "
                      f"Feels like {feels_like} degrees. "
                      f"Humidity is {humidity} percent.")
            print(result)
            self.speaker.say(result)
        except requests.exceptions.ConnectionError:
            self.speaker.say("No internet connection")
        except Exception as e:
            self.speaker.say("Something went wrong")
            print(f"Error: {e}")