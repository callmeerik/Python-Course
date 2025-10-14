import streamlit as st

# visual configuration
st.set_page_config(
    page_title="My App",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# styles to button
st.markdown("""
    <style>
            div.stButton > button:first-child {
                background-color: #FF4B4B;
                color: white;
                border-radius: 8px;
                height: 3em;
                width: 10em;
            }
    </style>
""", unsafe_allow_html=True)

st.title("New Streamlit App")

def greet():
    st.write("👋 Hello World")

greet_btn = st.button("Click Me!!")

if greet_btn:
    greet()

st.sidebar.header("Menu")
