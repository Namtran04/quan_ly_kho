import streamlit as st
import pandas as pd

def show_account_tab():
    st.title("🔑 Quản lý Tài khoản")
    
    # Khởi tạo dữ liệu tài khoản nếu chưa có
    if "accounts" not in st.session_state:
        st.session_state.accounts = pd.DataFrame(columns=[
            "Mã NV", "Tên đăng nhập", "Nhóm Quyền", "Trạng Thái"
        ])
    # Dữ liệu mẫu ban đầu
    if st.session_state.accounts.empty:
        sample_accounts = [
            {"Mã NV": "E001", "Tên đăng nhập": "admin", "Nhóm Quyền": "Admin", "Trạng Thái": "Hoạt động"},
            {"Mã NV": "E002", "Tên đăng nhập": "tranthib", "Nhóm Quyền": "Nhân viên", "Trạng Thái": "Hoạt động"},
            {"Mã NV": "E003", "Tên đăng nhập": "levanc", "Nhóm Quyền": "Nhân viên", "Trạng Thái": "Khóa"},
            {"Mã NV": "E004", "Tên đăng nhập": "phamthid", "Nhóm Quyền": "Nhân viên", "Trạng Thái": "Hoạt động"},
            {"Mã NV": "E005", "Tên đăng nhập": "hoangvane", "Nhóm Quyền": "Khách", "Trạng Thái": "Hoạt động"},
        ]
        st.session_state.accounts = pd.DataFrame(sample_accounts)
    
    # Hiển thị bảng dữ liệu tài khoản
    st.write("### Danh sách tài khoản")
    st.dataframe(st.session_state.accounts, use_container_width=True)

    # 🔍 Tìm kiếm tài khoản
    with st.expander("🔍 Tìm kiếm tài khoản"):
        search_query = st.text_input("Nhập từ khóa tìm kiếm:")
        if search_query:
            filtered_df = st.session_state.accounts[
                st.session_state.accounts.astype(str).apply(
                    lambda row: search_query.lower() in row.to_string().lower(), axis=1
                )
            ]
            st.write("### Kết quả tìm kiếm")
            st.dataframe(filtered_df, use_container_width=True)

    # ➕ Thêm tài khoản
    with st.expander("➕ Thêm tài khoản"):
        with st.form("add_account_form", clear_on_submit=True):
            employee_id = st.text_input("Mã nhân viên (Mã NV)")
            username = st.text_input("Tên đăng nhập")
            role = st.selectbox("Nhóm Quyền", ["Admin", "Nhân viên", "Khách"])
            status = st.selectbox("Trạng Thái", ["Hoạt động", "Khóa"])
            submitted = st.form_submit_button("Thêm")

            if submitted:
                if employee_id and username:
                    # Thêm dữ liệu mới vào DataFrame
                    new_row = {
                        "Mã NV": employee_id,
                        "Tên đăng nhập": username,
                        "Nhóm Quyền": role,
                        "Trạng Thái": status
                    }
                    st.session_state.accounts = pd.concat(
                        [st.session_state.accounts, pd.DataFrame([new_row])],
                        ignore_index=True
                    )
                    st.success("✅ Thêm tài khoản thành công!")
                    st.rerun()
                else:
                    st.error("❌ Vui lòng nhập đầy đủ thông tin bắt buộc!")

    # ✏️ Sửa tài khoản
    with st.expander("✏️ Sửa tài khoản"):
        account_to_edit = st.text_input("Nhập mã NV cần sửa")
        if account_to_edit:
            df = st.session_state.accounts
            if account_to_edit in df["Mã NV"].values:
                row_to_edit = df[df["Mã NV"] == account_to_edit].iloc[0]
                new_username = st.text_input("Tên đăng nhập", value=row_to_edit["Tên đăng nhập"])
                new_role = st.selectbox("Nhóm Quyền", ["Admin", "Nhân viên", "Khách"], index=["Admin", "Nhân viên", "Khách"].index(row_to_edit["Nhóm Quyền"]))
                new_status = st.selectbox("Trạng Thái", ["Hoạt động", "Khóa"], index=["Hoạt động", "Khóa"].index(row_to_edit["Trạng Thái"]))
                if st.button("Cập nhật"):
                    # Cập nhật dữ liệu trong DataFrame
                    st.session_state.accounts.loc[
                        df["Mã NV"] == account_to_edit, ["Tên đăng nhập", "Nhóm Quyền", "Trạng Thái"]
                    ] = [new_username, new_role, new_status]
                    st.success("✅ Cập nhật tài khoản thành công!")
                    st.rerun()
            else:
                st.error("❌ Mã NV không tồn tại!")

    # 🗑️ Xóa tài khoản
    with st.expander("🗑️ Xóa tài khoản"):
        account_to_delete = st.text_input("Nhập mã NV muốn xóa")
        if st.button("Xóa"):
            df = st.session_state.accounts
            if account_to_delete in df["Mã NV"].values:
                # Xóa dữ liệu trong DataFrame
                st.session_state.accounts = df[df["Mã NV"] != account_to_delete]
                st.success(f"✅ Đã xóa tài khoản có mã NV: {account_to_delete}")
                st.rerun()
            else:
                st.error("❌ Mã NV không tồn tại!")