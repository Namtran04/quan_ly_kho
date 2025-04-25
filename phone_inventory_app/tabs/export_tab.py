import streamlit as st

def show_export_tab():
    st.title("📤 Xuất danh sách sản phẩm")
    st.download_button(
        label="📥 Tải file",
        data=st.session_state.products.to_csv(index=False).encode('utf-8'),
        file_name="kho_hang.csv",
        mime="text/csv"
    )
    st.success("✅ Tải file thành công!")