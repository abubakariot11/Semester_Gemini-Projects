from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

# Importing google.generativeai with error handling
try:
    import google.generativeai as genai
except ImportError:
    st.error("Failed to import google.generativeai module. Please make sure it's installed correctly.")
    st.stop()

# Configure the API key using the value from the .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a GenerativeModel object
model = genai.GenerativeModel("gemini-pro")

# Function to generate response using Gemini model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Set Streamlit page configuration
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Text input box for user input
input_text = st.text_input("Input:", key="input")

# If input is provided, generate response and display it
if input_text:
    response = get_gemini_response(input_text)
    st.header("The Response is")
    st.write(response)


    