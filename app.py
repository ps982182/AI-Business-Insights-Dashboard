import streamlit as st
import pandas as pd 

st.title("AI Powered Business Insights Dashboard")

st.write("Upload your sales dataset")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df)