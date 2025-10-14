"""
Creation of data tables with Gemini
"""
import streamlit as st
from google import genai
from google.genai import types
import pandas as pd
from io import BytesIO
import re

st.set_page_config(
    page_title="Data Generation",
    page_icon="📊",
    layout="wide"
)

st.subheader("Data Table Generator")

def create_data_table(description):
    client = genai.Client(api_key= st.secrets.get("GEMINI_API_KEY"))
    try:

        response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
                You are an expert investigatorr.
                So create a data table in CSV format, using the next description: 
                {description}
                """,
                config= types.GenerateContentConfig(
                     temperature=0.2
                )
            )
    except Exception as ex:
            st.error(f"Error generating article: {ex}")
            return None
    return response.text

def create_excel_file(data):
    # convert csv file to dataframe
    raw_data = re.search(r"```csv\n([\s\S]*?)```", data)
    clean_data = raw_data.group(1).strip() if raw_data else data.strip()
    text_lines = [ line.strip() for line in clean_data.split('\n') if line.strip() ]
    if not text_lines:
        st.error("There are not data to process")
    
    # separate headings and data
    headers = text_lines[0].split(',')
    data_rows = [ line.split(',') for line in text_lines[1:] ]
    
    # create dataframe
    df = pd.DataFrame(data_rows, columns=headers)

    # save the df in excel file
    buffer = BytesIO()  # creating a binary stream
    with pd.ExcelWriter(buffer, engine="openpyxl") as file:
         df.to_excel(file, index=False, sheet_name="Data")

         #adjust the wide of columns
         worksheet = file.sheets['Data']
         for idx, col in enumerate(df.columns):
              max_lenght = max(df[col].astype(str).apply(len).max(), len(col))
              worksheet.column_dimensions[chr(65 + idx)].width = max_lenght + 2
    buffer.seek(0)
    return buffer, df

description = st.text_input("Write the description of data table")
if st.button("Generate table"):
     if description:
          with st.spinner("Generating Data"):
            data = create_data_table(description)
            if data:
                 st.success("✅ Data table created successfully")
                 excel_file, df = create_excel_file(data)

                 if excel_file and df is not None:
                      st.markdown("### Data Preview")
                      st.dataframe(df)

                      st.download_button(
                           label="Download Excel File",
                           data=excel_file,
                           file_name="data.xlsx",
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                      )
    