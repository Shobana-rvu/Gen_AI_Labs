from groq import Groq
import json
import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Read from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Example usage
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "Hello Groq!"}]
)

st.write(response.choices[0].message.content)




SYSTEM_PROMPT = """
You are a financial research agent.

Given a country name, identify:
1. Major stock exchanges in that country
2. Major benchmark stock indices

Return STRICT JSON ONLY in this format:

{
  "exchanges": ["Exchange Name"],
  "indices": {
    "Index Name": "Yahoo Finance Symbol"
  }
}

Rules:
- Use well-known exchanges only
- Use correct Yahoo Finance symbols
- Output valid JSON, nothing else
"""

def get_market_data(country: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": country}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()
    return json.loads(content)
