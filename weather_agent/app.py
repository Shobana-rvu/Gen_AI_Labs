
import streamlit as st
from agent import agent

st.set_page_config(page_title="Trip Planner Agent", layout="centered")

st.title("🌍 AI Trip Planner")
st.write("Plan your trip using real-time weather and AI insights")

user_prompt = st.text_input(
    "Ask about your trip",
    placeholder="How would the weather be for a 2 day trip to Udaipur in May?"
)

if st.button("Plan Trip"):
    if user_prompt:
        with st.spinner("Planning your trip..."):
            result = agent.invoke(user_prompt)
            response = result["messages"][0]["content"]
        st.success("Here's your travel insight:")
        st.write(response)
    else:
        st.warning("Please enter a prompt")