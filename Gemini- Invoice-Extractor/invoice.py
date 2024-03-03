from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vission')

def get_gemini_response(input, image, prompt):
    response = model.generate_content(inputs=[{"input": input}, {"image": image[0]}, {"prompt": prompt}])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    

# Set Streamlit page configuration
st.set_page_config(page_title="Multi Language Invoice Extractor")
st.header("Multi Language Invoice Extractor")

# Text input box for user input
input_text = st.text_input("Input Prompt:", key="input")

uploaded_file = st.file_uploader("choose an image of the invoice...", type=["jpg", "png", "jpeg", "gif"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Upload Image.", use_column_width=True)
    submit = st.button("Tell me about the invoice")

    input_prompt = """
    You are an expert in understanding invoices. We will upload image as invoice and you will
    have to answer any questions based on the uploaded invoice image.
    """

    if submit:
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(input_text, image_data, input_prompt)
        st.subheader("The Response is")
        st.write(response)
