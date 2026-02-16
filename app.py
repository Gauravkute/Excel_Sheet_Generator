import streamlit as st
import pandas as pd
import numpy as np
import random
import string
from datetime import datetime,timedelta


st.title("Data generator")

num_rows = st.number_input("Enter the number of rows",
                           min_value=1,
                           max_value=1000,
                           value=10)

num_cols = st.number_input("Enter the number of columns",
                           min_value=1,
                           max_value=20,
                           value=3)

file_name = st.text_input("Enter File Name", "generated_file")

file_format = st.selectbox(
    "Select File Format",
    ["xlsx","csv"]
)

columns = []
data_type = []

st.subheader("Define Columns")

for i in range(num_cols):
    col1,col2=st.columns(2)

    with col1:
        col_name = st.text_input(
            f"Column {i+1} Name",
            value=f"Column_{i+1}"
        )
    
    with col2:
        dtype = st.selectbox(
            f"Data Type for column {i+1}",
            ["Integer","Float","Text","Date"],
            key=i
        )
    
    columns.append(col_name)
    data_type.append(dtype)

    


def generate_data(dtype,rows):
    if dtype == "Integer":
        return np.random.randint(1,100,rows)
    elif dtype == "Float":
        return np.random.rand(rows)*10
    elif dtype == "Text":
        return[
            ''.join(random.choices(string.ascii_letters,k=5))
            for _ in range(rows)
        ]
    elif dtype == "Date":
        start_date = datetime.today()
        return[
            start_date - timedelta(days=random.randint(0,365))
            for _ in range (rows)
        ]

if st.button("Generate Data"):
    data = {}

    for col_name,dtype in zip(columns,data_type):
        data[col_name] = generate_data(dtype,num_rows)

    df = pd.DataFrame(data)
    st.dataframe(df)

    full_file_name = f"{file_name}.{file_format}"

    if file_format == "xlsx":
        df.to_excel(full_file_name,index=False)
    elif file_format == "csv":
        df.to_csv(full_file_name,index=False)

    with open(full_file_name,"rb") as file:
        st.download_button(
            label="Download data file",
            data=file,
            file_name=full_file_name,
            mime="application/octet-stream"
        )