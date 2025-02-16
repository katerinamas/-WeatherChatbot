import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from actions.weather import weather_city  
  # Import function

# Scenario 1: Get Temperature in a City
class ActionGetTemperature(Action):
    def name(self) -> str:
        return "action_get_temperature"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        city = tracker.get_slot("city")

        if not city:
            dispatcher.utter_message("I need to know the city. Can you specify one?")
            return []

        weather_info = weather_city(city, use_API=True)

        if "error" in weather_info:
            dispatcher.utter_message(f"Error fetching weather: {weather_info['error']}")
            return []

        temperature = weather_info.get("temperature")
        feels_like = weather_info.get("feels_like")

        response = (
            f"🌡️ The temperature in {weather_info['city']}, {weather_info['country']} is {temperature}°C, "
            f"but it feels like {feels_like}°C."
        )
        dispatcher.utter_message(response)
        return []

# Scenario 2: Get Weather Situation in a City
class ActionGetWeatherSituation(Action):
    def name(self) -> str:
        return "action_get_weather_situation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        city = tracker.get_slot("city")

        if not city:
            dispatcher.utter_message("I need to know the city. Can you specify one?")
            return []

        weather_info = weather_city(city, use_API=True)

        if "error" in weather_info:
            dispatcher.utter_message(f"Error fetching weather: {weather_info['error']}")
            return []

        condition = weather_info.get("weather")
        humidity = weather_info.get("humidity")
        wind_speed = weather_info.get("wind_speed")

        response = (
            f"🌤️ In {weather_info['city']}, {weather_info['country']}, the weather is {condition}.\n"
            f"- Humidity: {humidity}%\n"
            f"- Wind Speed: {wind_speed} m/s"
        )
        dispatcher.utter_message(response)
        return []

#  Scenario 3: Get Sunrise Time in a City
class ActionGetSunriseTime(Action):
    def name(self) -> str:
        return "action_get_sunrise_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        import datetime

        city = tracker.get_slot("city")

        if not city:
            dispatcher.utter_message("I need to know the city. Can you specify one?")
            return []

        weather_info = weather_city(city, use_API=True)

        if "error" in weather_info:
            dispatcher.utter_message(f"Error fetching weather: {weather_info['error']}")
            return []

        sunrise_timestamp = weather_info.get("sunrise")
        sunrise_time = datetime.datetime.utcfromtimestamp(sunrise_timestamp).strftime('%H:%M:%S UTC')

        response = f"🌅 The sun rises in {weather_info['city']} at {sunrise_time}."
        dispatcher.utter_message(response)
        return []
