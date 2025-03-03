import streamlit as st
import requests  # Import the requests library for HTTP requests

# Streamlit UI
st.title("🔗 HTTP Client with Streamlit")

# Text input fields
user_name = st.text_input("Enter your name:")
text_prompt = st.text_input("Enter your text prompt:")

# Ngrok URL
NGROK_URL = "http://1234abcd.ngrok.io/receive_data"  # Replace with your actual ngrok URL

# Submit button
if st.button("Send Message"):
    if user_name.strip() and text_prompt.strip():
        # Create the data payload
        data = {
            "name": user_name,
            "text_prompt": text_prompt
        }

        try:
            # Send a POST request to the ngrok endpoint
            response = requests.post(NGROK_URL, json=data)
            if response.status_code == 200:
                st.success("✅ Message sent successfully!")
                st.write(f"📤 Sent: Name - {user_name}, Text Prompt - {text_prompt}")
            else:
                st.error("⚠️ Failed to send message. Server responded with an error.")
                
        except requests.exceptions.RequestException as e:
            st.error(f"⚠️ Connection error: {e}")
    else:
        st.warning("Please enter messages in both fields before submitting.")
