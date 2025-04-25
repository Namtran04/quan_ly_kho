import streamlit as st
from utils.excel_handler import read_excel

def show_import_tab():
    st.title("📥 Nhập dữ liệu từ Excel")
    uploaded_file = st.file_uploader("📂 Chọn file", type=["xlsx"])
    if uploaded_file:
        df_new = read_excel(uploaded_file)
        st.session_state.products = st.session_state.products._append(df_new, ignore_index=True)
        st.success("✅ Dữ liệu đã được nhập!")
        st.rerun()