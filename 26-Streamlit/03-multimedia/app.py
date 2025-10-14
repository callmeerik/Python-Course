import streamlit as st
from PIL import Image  # image manipulation library pillow

def main():
    st.title("Multimedia with Streamlit")

    st.subheader("Image")
    img = Image.open("./assets/simpson.jpeg")
    st.image(img)

    st.subheader("Video")
    with open("./assets/watermelon.mp4", "rb") as video_file:
        st.video(video_file, format="video/mp4", start_time=0)

    st.subheader("Audio")
    with open("./assets/zombie.mp4", "rb") as music_file:
        st.audio(music_file)

if __name__ == "__main__":
    main()