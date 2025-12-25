import streamlit as st
import requests

st.title("My Python Super App 🐍")

# Create Tabs for your 3 screens
tab1, tab2, tab3,tab4 = st.tabs(["🤖 AI Chat", "📜 History", "☁️ Weather", "city"])

# --- TAB 1: AI CHAT ---
with tab1:
    st.header("Talk to Llama 3")
    user_input = st.text_input("What is on your mind?")

    if st.button("Send to AI"):
        # This calls YOUR FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/chat", json={"prompt": user_input}
        )
        st.write(response.json())

# --- TAB 2: HISTORY ---
with tab2:
    st.header("Past Conversations")
    if st.button("Refresh History"):
        response = requests.get("http://127.0.0.1:8000/data")
        st.write(response.json())

# --- TAB 3: WEATHER ---
with tab3:
    st.header("Check Weather")
    city = st.text_input("Type a City Name")
    if st.button("Get Weather"):
        # We use your Backend to search and get weather
        response = requests.post(
            "http://127.0.0.1:8000/weather_data", json={"city": city}
        )
        st.write(response.json())
with tab4:
    st.header("City Name")
    city =st.text_input("Name of the city")
    if st.button("city"):
        response=requests.post(
            "http://127.0.0.1:8000/search_city", json={"query": city}
        )
        st.write(response.json())