import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt as dx
from PyPDF2 import PdfReader

@st.cache_data  # store data in cache memory
def load_img(img_file):
    img = Image.open(img_file)
    return img

def read_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    txt = ""
    for pg in range(num_pages):
        page = pdf_reader.pages[pg]
        txt += page.extract_text()
    return txt

# main function
def main():
    st.title("Load Files With Streamlit")
    menu = ["Images", "DataFrames", "Documents"]
    st.sidebar.header("Menu")
    choose = st.sidebar.radio("Select an option to upload file", menu)

    # compare selection
    if choose == "Images":
        st.header("Image")
        file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        st.subheader("Image Details")
        if file:
            st.write(f"Name: {file.name}")
            st.write(f"Size: {file.size}")
            st.write(f"Type: {file.type}")

            # show the image
            st.image(load_img(file), width=200)
        else:
            st.write("No file selected")
    elif choose == "DataFrames":
        st.header("DataFrames")
        file = st.file_uploader("Select a file, CSV or XLSX", type=["csv", "xlsx"])
        if file:
            st.write(f"Name: {file.name}")
            st.write(f"Size: {file.size}")
            st.write(f"Type: {file.type}")
            if file.type == "text/csv" or file.type == "application/vnd.ms-excel":
                df = pd.read_csv(file)
            elif file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(file)
            else:
                df = pd.DataFrame()
            st.dataframe(df)
    elif choose == "Documents":
        st.header("Documents ")
        file = st.file_uploader("Select a file, Word, Txt, PDF", type=["docx", "txt", "pdf"])
        
        if file:
            st.write(f"Name: {file.name}")
            st.write(f"Size: {file.size}")
            st.write(f"Type: {file.type}")
            if file.type == "text/plain":
                text = str(file.read(), encoding="utf-8")
                st.text_area("Extracted Text",text, height=400)
            elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                doc_txt = dx.process(file)
                st.text_area("Extracted text", doc_txt, height=500)
            elif file.type == "application/pdf":
                # text extraction
                #pdf_txt = read_pdf(file)
                #st.text_area("PDF Extracted Text", pdf_txt, height=500)
                st.pdf(file)
                



if __name__ == "__main__":
    main()