import pandas as pd
import openpyxl as xl
import streamlit as st

def get_data_from_excel():
    df = pd.read_excel(io="C:\\Users\\tranp\\OneDrive\\Desktop\\vscode\\.vscode\\nuedu-1968847653609394.xlsx",
                  engine="openpyxl",
                  sheet_name="Sheet",
                  skiprows=3,
                  usecols="A:C",
                  nrows=123)
    return df

df = get_data_from_excel()

print(df)