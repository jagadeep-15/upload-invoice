import streamlit as st
import pandas as pd
import json

# Set the Streamlit page configuration
st.set_page_config(page_title="Invoice Upload", page_icon="🧾", layout="wide")

# Upload file section
uploaded_file = st.file_uploader("Upload your invoice", type=["pdf", "jpg", "png", "jpeg", "xls", "xlsx", "json"])

# Create a placeholder for dynamic content
placeholder = st.empty()

if uploaded_file is not None:
    # Clear previous content and display the new file content
    placeholder.empty()  # Clears previous content in the placeholder
    
    # Process the file based on its type
    if uploaded_file.type in ["application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        try:
            df = pd.read_excel(uploaded_file)
            st.write("### Detailed Invoice Data")
            st.dataframe(df)
        except ImportError:
            st.error("Missing optional dependency 'openpyxl'. Please install it using `pip install openpyxl`.")
    elif uploaded_file.type == "application/json":
        try:
            data = json.load(uploaded_file)
            st.write("### JSON File Content")
            st.json(data)
        except json.JSONDecodeError:
            st.error("Error decoding JSON file. Please upload a valid JSON file.")
    else:
        st.write("Uploaded file type is not supported. Please upload an Excel or JSON file.")

# Sidebar content
st.sidebar.image("https://www.example.com/your-logo.png", use_column_width=True)
st.sidebar.markdown("# Invoice Upload App")
st.sidebar.markdown("Use this app to upload and view your invoices.")
