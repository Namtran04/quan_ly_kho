import streamlit as st
import pandas as pd

def show_supplier_tab():
    st.title("🏢 Nhà cung cấp")
    
    # Khởi tạo dữ liệu nhà cung cấp nếu chưa có
    if "suppliers" not in st.session_state:
        st.session_state.suppliers = pd.DataFrame([
            {"Mã NCC": "NCC001", "Tên nhà cung cấp": "Công ty A", "Địa chỉ": "Hà Nội", "Email": "contact@congtya.com", "Số điện thoại": "0123456789"},
            {"Mã NCC": "NCC002", "Tên nhà cung cấp": "Công ty B", "Địa chỉ": "TP.HCM", "Email": "contact@congtyb.com", "Số điện thoại": "0987654321"}
        ])
    
    # Hiển thị bảng dữ liệu nhà cung cấp
    st.write("### Danh sách nhà cung cấp")
    st.dataframe(st.session_state.suppliers, use_container_width=True)

    # 🔍 Tìm kiếm nhà cung cấp
    with st.expander("🔍 Tìm kiếm nhà cung cấp"):
        search_query = st.text_input("Nhập từ khóa tìm kiếm:")
        if search_query:
            filtered_df = st.session_state.suppliers[
                st.session_state.suppliers.astype(str).apply(
                    lambda row: search_query.lower() in row.to_string().lower(), axis=1
                )
            ]
            st.write("### Kết quả tìm kiếm")
            st.dataframe(filtered_df, use_container_width=True)

    # ➕ Thêm nhà cung cấp
    with st.expander("➕ Thêm nhà cung cấp"):
        with st.form("add_supplier_form", clear_on_submit=True):
            supplier_id = st.text_input("Mã NCC")
            supplier_name = st.text_input("Tên nhà cung cấp")
            address = st.text_input("Địa chỉ")
            email = st.text_input("Email")
            phone = st.text_input("Số điện thoại")
            submitted = st.form_submit_button("Thêm")

            if submitted:
                if supplier_id and supplier_name and phone:
                    # Thêm dữ liệu mới vào DataFrame
                    new_row = {
                        "Mã NCC": supplier_id,
                        "Tên nhà cung cấp": supplier_name,
                        "Địa chỉ": address,
                        "Email": email,
                        "Số điện thoại": phone
                    }
                    st.session_state.suppliers = pd.concat(
                        [st.session_state.suppliers, pd.DataFrame([new_row])],
                        ignore_index=True
                    )
                    st.success("✅ Thêm nhà cung cấp thành công!")
                    st.rerun()  # Làm mới giao diện
                else:
                    st.error("❌ Vui lòng nhập đầy đủ thông tin bắt buộc!")

    # ✏️ Sửa nhà cung cấp
    with st.expander("✏️ Sửa nhà cung cấp"):
        supplier_id_to_edit = st.text_input("Nhập mã NCC cần sửa")
        if supplier_id_to_edit:
            df = st.session_state.suppliers
            if supplier_id_to_edit in df["Mã NCC"].values:
                row_to_edit = df[df["Mã NCC"] == supplier_id_to_edit].iloc[0]
                new_name = st.text_input("Tên nhà cung cấp", value=row_to_edit["Tên nhà cung cấp"])
                new_address = st.text_input("Địa chỉ", value=row_to_edit["Địa chỉ"])
                new_email = st.text_input("Email", value=row_to_edit["Email"])
                new_phone = st.text_input("Số điện thoại", value=row_to_edit["Số điện thoại"])
                if st.button("Cập nhật"):
                    # Cập nhật dữ liệu trong DataFrame
                    st.session_state.suppliers.loc[
                        df["Mã NCC"] == supplier_id_to_edit, ["Tên nhà cung cấp", "Địa chỉ", "Email", "Số điện thoại"]
                    ] = [new_name, new_address, new_email, new_phone]
                    st.success("✅ Cập nhật nhà cung cấp thành công!")
                    st.rerun()  # Làm mới giao diện
            else:
                st.error("❌ Mã NCC không tồn tại!")

    # 🗑️ Xóa nhà cung cấp
    with st.expander("🗑️ Xóa nhà cung cấp"):
        supplier_id_to_delete = st.text_input("Nhập mã NCC muốn xóa")
        if st.button("Xóa"):
            df = st.session_state.suppliers
            if supplier_id_to_delete in df["Mã NCC"].values:
                # Xóa dữ liệu trong DataFrame
                st.session_state.suppliers = df[df["Mã NCC"] != supplier_id_to_delete]
                st.success(f"✅ Đã xóa nhà cung cấp có mã NCC: {supplier_id_to_delete}")
                st.rerun()  # Làm mới giao diện
            else:
                st.error("❌ Mã NCC không tồn tại!")