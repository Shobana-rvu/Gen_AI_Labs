from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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