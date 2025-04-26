import streamlit as st
import pandas as pd
from datetime import datetime

def show_customer_tab():
    st.title("👥 Quản lý Khách hàng")

    # Khởi tạo dữ liệu khách hàng nếu chưa có
    if "customers" not in st.session_state:
        st.session_state.customers = pd.DataFrame(columns=[
            "Mã Khách Hàng", "Tên Khách Hàng", "Địa Chỉ", "Số Điện Thoại", "Ngày Tham Gia"
        ])

    # Dữ liệu mẫu ban đầu
    if st.session_state.customers.empty:
        sample_customers = [
            {"Mã Khách Hàng": "C001", "Tên Khách Hàng": "Nguyễn Văn A", "Địa Chỉ": "Hà Nội", "Số Điện Thoại": "0901234567", "Ngày Tham Gia": "2025-01-01"},
            {"Mã Khách Hàng": "C002", "Tên Khách Hàng": "Trần Thị B", "Địa Chỉ": "Hồ Chí Minh", "Số Điện Thoại": "0912345678", "Ngày Tham Gia": "2025-02-15"},
            {"Mã Khách Hàng": "C003", "Tên Khách Hàng": "Lê Văn C", "Địa Chỉ": "Đà Nẵng", "Số Điện Thoại": "0923456789", "Ngày Tham Gia": "2025-03-10"},
            {"Mã Khách Hàng": "C004", "Tên Khách Hàng": "Phạm Thị D", "Địa Chỉ": "Hải Phòng", "Số Điện Thoại": "0934567890", "Ngày Tham Gia": "2025-04-01"},
            {"Mã Khách Hàng": "C005", "Tên Khách Hàng": "Hoàng Văn E", "Địa Chỉ": "Cần Thơ", "Số Điện Thoại": "0945678901", "Ngày Tham Gia": "2025-04-10"},
        ]
        st.session_state.customers = pd.DataFrame(sample_customers)

    # Hiển thị bảng dữ liệu khách hàng
    st.write("### Danh sách khách hàng")
    st.dataframe(st.session_state.customers, use_container_width=True)

    # 🔍 Tìm kiếm khách hàng
    with st.expander("🔍 Tìm kiếm khách hàng"):
        search_query = st.text_input("Nhập từ khóa tìm kiếm:")
        if search_query:
            filtered_df = st.session_state.customers[
                st.session_state.customers.astype(str).apply(
                    lambda row: search_query.lower() in row.to_string().lower(), axis=1
                )
            ]
            st.write("### Kết quả tìm kiếm")
            st.dataframe(filtered_df, use_container_width=True)

    # ➕ Thêm khách hàng
    with st.expander("➕ Thêm khách hàng"):
        with st.form("add_customer_form", clear_on_submit=True):
            customer_id = st.text_input("Mã Khách Hàng")
            customer_name = st.text_input("Tên Khách Hàng")
            address = st.text_input("Địa Chỉ")
            phone = st.text_input("Số Điện Thoại")
            join_date = st.date_input("Ngày Tham Gia", value=datetime.now())
            submitted = st.form_submit_button("Thêm")

            if submitted:
                if customer_id and customer_name and phone:
                    # Thêm dữ liệu mới vào DataFrame
                    new_row = {
                        "Mã Khách Hàng": customer_id,
                        "Tên Khách Hàng": customer_name,
                        "Địa Chỉ": address,
                        "Số Điện Thoại": phone,
                        "Ngày Tham Gia": join_date.strftime("%Y-%m-%d")
                    }
                    st.session_state.customers = pd.concat(
                        [st.session_state.customers, pd.DataFrame([new_row])],
                        ignore_index=True
                    )
                    st.success("✅ Thêm khách hàng thành công!")
                    st.rerun()
                else:
                    st.error("❌ Vui lòng nhập đầy đủ thông tin!")

    # ✏️ Sửa khách hàng
    with st.expander("✏️ Sửa khách hàng"):
        if not st.session_state.customers.empty:
            row_to_edit = st.selectbox("Chọn dòng để sửa", st.session_state.customers.index)
            if row_to_edit is not None:
                selected_row = st.session_state.customers.loc[row_to_edit]
                customer_id = st.text_input("Mã Khách Hàng", value=selected_row["Mã Khách Hàng"])
                customer_name = st.text_input("Tên Khách Hàng", value=selected_row["Tên Khách Hàng"])
                address = st.text_input("Địa Chỉ", value=selected_row["Địa Chỉ"])
                phone = st.text_input("Số Điện Thoại", value=selected_row["Số Điện Thoại"])
                join_date = st.date_input("Ngày Tham Gia", value=pd.to_datetime(selected_row["Ngày Tham Gia"]))
                if st.button("Cập nhật"):
                    # Cập nhật dữ liệu
                    st.session_state.customers.loc[row_to_edit] = {
                        "Mã Khách Hàng": customer_id,
                        "Tên Khách Hàng": customer_name,
                        "Địa Chỉ": address,
                        "Số Điện Thoại": phone,
                        "Ngày Tham Gia": join_date.strftime("%Y-%m-%d")
                    }
                    st.success("✅ Cập nhật khách hàng thành công!")
                    st.rerun()

    # 🗑️ Xóa khách hàng
    with st.expander("🗑️ Xóa khách hàng"):
        if not st.session_state.customers.empty:
            row_to_delete = st.selectbox("Chọn dòng để xóa", st.session_state.customers.index)
            if st.button("Xóa"):
                st.session_state.customers = st.session_state.customers.drop(index=row_to_delete).reset_index(drop=True)
                st.success("✅ Xóa khách hàng thành công!")
                st.rerun()