import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.title("Content Generator with Gemini AI API")

st.write("This app is a content generator, using GPT-4o model from OpenAI")

st.markdown("""
### **Content**
1. Article Generator
2. Code Generator
3. Dataset Generator
""")