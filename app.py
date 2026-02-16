import streamlit as st
import pandas as pd
import numpy as np
import random
import string
from datetime import datetime,timedelta


st.title("Excel Sheet Generator")

num_rows = st.number_input("Enter the number of rows",
                           min_value=1,
                           max_value=1000,
                           value=10)

num_cols = st.number_input("Enter the number of columns",
                           min_value=1,
                           max_value=20,
                           value=3)

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

if st.button("Generate Excel Sheet"):
    data = {}

    for col_name,dtype in zip(columns,data_type):
        data[col_name] = generate_data(dtype,num_rows)

    df = pd.DataFrame(data)
    st.dataframe(df)

    file_name = "generated_excel_sheet.xlsx"
    df.to_excel(file_name,index=False)

    with open(file_name,"rb") as file:
        st.download_button(
            label="Download Excel sheet file",
            data=file,
            file_name=file_name

        )