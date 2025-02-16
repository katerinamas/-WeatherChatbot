# -WeatherChatbot🌤️ 🌡️
A chatbot built with Rasa 3.1 that provides real-time weather updates, including temperature, weather conditions, and sunrise time for any city using an API from OpenWeatherMap 
This chatbot specializes in providing real-time weather updates based on user queries. The primary motivation for choosing this domain includes:

Convenience – Users can get instant weather updates without browsing through websites or apps.
Efficiency – A conversational bot offers a faster way to get specific weather details.
API Integration – Demonstrates the ability to work with external APIs for real-world applications.

Implemented Scenarios
The chatbot supports the following scenarios:

✅ Scenario 1: Get Temperature for a City
User Input: "What's the temperature in New York?"
Bot Response: "The temperature in New York is 1.51°C, but it feels like -2.51°C."

✅ Scenario 2: Get Weather Conditions for a City
User Input: "How's the weather in Berlin?"
Bot Response: "In Berlin, DE, the weather is overcast clouds. Humidity: 77%. Wind Speed: 3.13 m/s"

✅ Scenario 3: Get Sunrise Time for a City
User Input: "Sunrise time in Berlin?"
Bot Response: "The sun rises in Berlin at 06:22:45 UTC."

✅ Scenario 4: Handle Missing City
User Input: "When is the sunrise?"
Bot Response: "I need to know the city. Can you specify one??"
User: "Athens"
Bot: "🌅 The sun rises in Athens at 05:14:09 UTC."

✅ Scenario 5: Answer General Queries
"Who are you?" → "I’m WeatherBot, your weather assistant. ☁️ I provide weather updates and forecasts."
"What can you do?" → "I can provide weather updates and details like temperature 🌡️, wind 💨, rain 🌧️, and sunrise 🌅 times."

✅ Scenario 6: Handle Irrelevant Questions
User Input: "Do you believe in aliens?"
Bot Response: "I focus on weather updates 🌦️. Let me know if you need a forecast!"

Integrated Data Source
The bot fetches real-time weather data using OpenWeather API:

 API URL: https://openweathermap.org/api
 
 Authentication: Requires a free API key (signup at OpenWeather)
 
 Data Provided:
Temperature
Weather conditions
Wind speed
Humidity
Sunrise/Sunset times

Challenges & Solutions
1️⃣ Handling Missing User Input
Problem: Users often ask for the weather without specifying a city, leading to failed API calls.
Solution: Implemented a fallback mechanism where the bot asks for the missing city before proceeding. 

2️⃣ Ensuring API Reliability
Problem: The OpenWeather API might fail due to incorrect input, missing API keys, or rate limits.
Solution: Added error handling:
If the API key is missing/invalid, the bot informs the user.
If the API request fails, the bot displays a friendly error message instead of crashing.
If the API is rate-limited, the bot provides a static response.

3️⃣ Improving Natural Language Understanding (NLU)
Problem: Users phrase questions differently, e.g., "How's the weather?" vs. "Tell me if it's raining."
Solution:
Expanded training data in nlu.yml to recognize multiple variations.

4️⃣ Handling Unexpected or Irrelevant Queries
Problem: Users may ask off-topic questions, such as "Tell me a joke" or "What’s 2 + 2?"
Solution:
Added an “out_of_scope” intent.
Trained the bot to recognize off-topic inputs and respond politely.
Provided a fallback response suggesting valid queries.

Setup Guide
1. Install Dependencies
Ensure you have Python 3.8+ and Rasa installed
2. Clone the respitory https://github.com/katerinamas/-WeatherChatbot.git
3. Set Up API Key
Get a free API key from OpenWeather and set it in the weather.py (API_key=)
4. Train the model with Rasa train
5. Start the Rasa Action Server with Rasa run actions
6. Run the Chatbot with Rasa shell
7. Try asking "How is the weather in Rome?"

Dialogue Policy Experimentation

In this chatbot implementation, we have used several Rasa policies to optimize dialogue management and ensure accurate responses. Below is a breakdown of the policies we used and the reasoning behind these choices:

Memoization Policy (max_history: 6) – Ensures consistency by remembering past interactions and improving repetitive queries.
TED Policy (max_history: 8, epochs: 150) – Enhances prediction accuracy by considering longer conversation context and refining training over multiple iterations.
Rule Policy (fallback handling enabled) – Manages predefined interactions like greetings while ensuring deterministic responses.
Fallback Classifier (threshold: 0.4, ambiguity_threshold: 0.2) – Prevents incorrect responses by triggering fallback messages for low-confidence predictions.
