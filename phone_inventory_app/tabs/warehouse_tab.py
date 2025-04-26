import streamlit as st
import pandas as pd

def show_warehouse_tab():
    st.title("📍 Khu vực kho")
    
    # Khởi tạo dữ liệu khu vực kho nếu chưa có
    if "warehouses" not in st.session_state:
        st.session_state.warehouses = pd.DataFrame(columns=["Mã kho", "Khu vực", "Ghi chú"])

    # Dữ liệu mẫu ban đầu
    if st.session_state.warehouses.empty:
        sample_warehouses = [
            {"Mã kho": "W001", "Khu vực": "Hà Nội", "Ghi chú": "Kho chính"},
            {"Mã kho": "W002", "Khu vực": "Hồ Chí Minh", "Ghi chú": "Kho phụ"},
            {"Mã kho": "W003", "Khu vực": "Đà Nẵng", "Ghi chú": "Kho miền Trung"},
            {"Mã kho": "W004", "Khu vực": "Hải Phòng", "Ghi chú": "Kho miền Bắc"},
            {"Mã kho": "W005", "Khu vực": "Cần Thơ", "Ghi chú": "Kho miền Tây"},
        ]
        st.session_state.warehouses = pd.DataFrame(sample_warehouses)
    # 🔍 Tìm kiếm khu vực kho
    search_query = st.text_input("🔍 Nhập từ khóa tìm kiếm:")
    if search_query:
        filtered_df = st.session_state.warehouses[
            st.session_state.warehouses.astype(str).apply(
                lambda row: search_query.lower() in row.to_string().lower(), axis=1
            )
        ]
        st.write("### Kết quả tìm kiếm")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        # Hiển thị bảng dữ liệu khu vực kho
        st.write("### Danh sách khu vực kho")
        st.dataframe(st.session_state.warehouses, use_container_width=True)

    # ➕ Thêm khu vực kho
    with st.expander("➕ Thêm khu vực kho"):
        with st.form("add_warehouse_form", clear_on_submit=True):
            warehouse_id = st.text_input("Mã kho")
            area = st.text_input("Khu vực")
            note = st.text_input("Ghi chú")
            submitted = st.form_submit_button("Thêm")

            if submitted:
                if warehouse_id and area:
                    # Thêm dữ liệu mới vào DataFrame
                    new_row = {"Mã kho": warehouse_id, 
                               "Khu vực": area, 
                               "Ghi chú": note}
                    st.session_state.warehouses = pd.concat(
                        [st.session_state.warehouses, pd.DataFrame([new_row])],
                        ignore_index=True
                    )
                    st.success("✅ Thêm khu vực kho thành công!")
                    st.rerun()
                else:
                    st.error("❌ Vui lòng nhập đầy đủ thông tin!")

    # ✏️ Sửa khu vực kho
    with st.expander("✏️ Sửa khu vực kho"):
        warehouse_id_to_edit = st.text_input("Nhập mã kho cần sửa")
        if warehouse_id_to_edit:
            df = st.session_state.warehouses
            if warehouse_id_to_edit in df["Mã kho"].values:
                row_to_edit = df[df["Mã kho"] == warehouse_id_to_edit].iloc[0]
                new_area = st.text_input("Khu vực", value=row_to_edit["Khu vực"])
                new_note = st.text_input("Ghi chú", value=row_to_edit["Ghi chú"])
                if st.button("Cập nhật"):
                    st.session_state.warehouses.loc[
                        df["Mã kho"] == warehouse_id_to_edit, ["Khu vực", "Ghi chú"]
                    ] = [new_area, new_note]
                    st.success("✅ Cập nhật khu vực kho thành công!")
                    st.rerun()
            else:
                st.error("❌ Mã kho không tồn tại!")

    # 🗑️ Xóa khu vực kho
    with st.expander("🗑️ Xóa khu vực kho"):
        warehouse_id_to_delete = st.text_input("Nhập mã kho muốn xóa")
        if st.button("Xóa"):
            df = st.session_state.warehouses
            if warehouse_id_to_delete in df["Mã kho"].values:
                st.session_state.warehouses = df[df["Mã kho"] != warehouse_id_to_delete]
                st.success(f"✅ Đã xóa khu vực kho có mã kho: {warehouse_id_to_delete}")
            else:
                st.error("❌ Mã kho không tồn tại!")