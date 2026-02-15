import streamlit as st
import pandas as pd
import numpy as np
import openpyxl

st.title("Excel Sheet Generator")

num_rows = st.number_input("Enter the number of rows",min_value=1,max_value=1000,value=10)

if st.button("Generate Excel sheet"):
    data={
        "ID":np.arange(1,num_rows+1),
        "Random Number":np.random.randint(1,100,num_rows),
        "Random Floats":np.random.rand(num_rows)
    }
    df = pd.DataFrame(data)

    st.dataframe(df)

    file_name="excel_sheet.xlsx"
    df.to_excel(file_name,index=False)
    with open(file_name,"rb") as file:
        st.download_button(
            label="Download Excel file",
            data=file,
            file_name=file_name,         
        )