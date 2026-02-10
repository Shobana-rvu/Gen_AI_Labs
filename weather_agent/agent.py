import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from weather_tool import get_weather
import streamlit as st

load_dotenv()

llm = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model_name="llama-3.1-8b-instant"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a travel assistant. When asked about weather, extract the city name and provide weather information."),
    ("user", "{input}")
])

class SimpleAgent:
    def invoke(self, user_input):
        # Extract city from user input
        city_prompt = f"Extract only the city name from this query: '{user_input}'. Reply with just the city name, nothing else."
        city_response = llm.invoke(city_prompt)
        city = city_response.content.strip()
        
        # Get weather
        weather_data = get_weather(city)
        
        # Generate response
        final_prompt = f"User asked: {user_input}\n\nWeather data for {city}: {weather_data}\n\nProvide a helpful travel response."
        response = llm.invoke(final_prompt)
        
        return {"messages": [{"content": response.content}]}

agent = SimpleAgent()
