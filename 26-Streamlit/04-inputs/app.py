import streamlit as st

def main():
    st.title("User Input With Streamlit")

    name = st.text_input("Enter your name")
    st.write(name)
    age = st.number_input("Enter your age", min_value=0, max_value=100, step=1)
    comment = st.text_area("Enter your comment")
    color = st.color_picker("Choose a color")
    birth_date = st.date_input("Enter your birth date")
    time = st.time_input("Enter the meeting time")

if __name__ == '__main__':
    main()