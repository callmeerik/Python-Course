import streamlit as st
from football import get_data
from image import get_image_details
def main():
    menu = ["Football Dataframe", "Image Metadata Viewer"]
    st.sidebar.header("Menu")
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Football Dataframe":
        get_data()
    elif choice == "Image Metadata Viewer":
        get_image_details()

if __name__ == "__main__":
    main()