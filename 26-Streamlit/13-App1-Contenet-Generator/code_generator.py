"""
Code generator
"""
import streamlit as st
from google import genai
from google.genai import types
import re  # manage regular expressions

st.set_page_config(
    page_title="Ai Code Generator",
    page_icon="💻",
    layout="wide"
)
st.subheader("Code Generator with Gemini")

def generate_code(topic, language):
    client = genai.Client(api_key= st.secrets.get("GEMINI_API_KEY"))
    try:

        response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
                You are an expert software developer.
                Write a code about {topic} in {language} languagr, give me only the code
                """,
                config= types.GenerateContentConfig(
                     temperature=0.2
                )
            )
    except Exception as ex:
            st.error(f"Error generating article: {ex}")
            return None
    return response.text

description = st.text_area("Write the descriptiion of code", height=100)
language_info = {
    "Python": (".py", "text/x-python"),
    "JavaScript": (".js", "application/javascript"),
    "C++": (".cpp", "text/x-c++src"),
    "Java": (".java", "text/x-java-source"),
    "HTML": (".html", "text/html"),
    "CSS": (".css", "text/css"),
    "C#": (".cs", "text/x-csharp"),
    "Go": (".go", "text/x-go"),
}

language_selection = st.pills(
     "Select a programming language",
     list(language_info.keys())
)

if st.button(f"Generate Code"):
     if description and language_selection:
          with st.spinner("Generating Code..."):
                raw_code = generate_code(description, language_selection)
                # extract code
                match =  re.search(r"```[a-zA-Z0-9+#]*\n([\s\S]*?)```", raw_code)
                clean_code = match.group(1).strip() if match else raw_code.strip()

                if clean_code:
                    st.success("✅ Code generated")
                    st.code(clean_code, language=f"{language_selection.lower()}")
                    ext, mime = language_info[language_selection]
                    st.download_button(
                         label=f"📥 Download {language_selection} File",
                         data=clean_code,
                         file_name=f"code{ext}",
                         mime= mime
                    )