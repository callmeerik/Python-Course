import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS   # extract metadata from images

def get_image_details():
    st.title("📸 Image Metada Viewer")
    file = st.file_uploader("select an image", type=["png", "jpg", "jpeg"])
    if file:
        # open image
        img = Image.open(file)

        # show imag
        st.image(img, caption=file.name)

        # extract metadata
        img_data = img.getexif()   # return an object dictionary

        if img_data:
            metadata = {}
            for tag_id, value in img_data.items():
                # get tags
                tag = TAGS.get(tag_id, tag_id)
                metadata[tag] = value
            # convert the dictionary to a json object
            st.json(metadata)
        else:
            st.warning("No Exif Metadata available")