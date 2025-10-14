import streamlit as st

def main():
    st.title("Select in Streamlit")

    country = st.selectbox(
        "Choose your country",
        ["Ecuador", "Spain", "Brazil", "Colombia"]
    )
    st.write(f"Your country: {country}")

    fav_languages = st.multiselect(
        "Select your favs programming languages",
         ["Python", "Java", "C++", "C", "C#", "Rust", "Go", "JavaScript", "PHP"]
    )
    st.write(fav_languages)

    # slider
    price = st.slider(
        "Select your price range",
        min_value=0,
        max_value=250,
        step=1,
        value=0
    )
    st.write(price)

    scale = st.select_slider(
        "Select your feeling",
        ["Very Sad", "Sad", "Normal", "Happy", "Very Happy"]
    )
    st.write(scale)

    gender = st.radio(
        "Select your gender",
        ["Male", "Female"]
    )
    st.write(gender)

if __name__ == '__main__':
    main()