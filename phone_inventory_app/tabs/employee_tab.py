import streamlit as st
import pandas as pd

def show_employee_tab():
    st.title("👨‍💼 Nhân viên")
    
    # Khởi tạo dữ liệu nhân viên nếu chưa có
    if "employees" not in st.session_state:
        st.session_state.employees = pd.DataFrame(columns=[
            "MNV", "Họ và Tên", "Giới Tính", "Ngày Sinh", "Số Điện Thoại", "Email"
        ])
     # Dữ liệu mẫu ban đầu
    if st.session_state.employees.empty:
        sample_employees = [
            {"MNV": "E001", "Họ và Tên": "Nguyễn Văn A", "Giới Tính": "Nam", "Ngày Sinh": "1990-01-01", "Số Điện Thoại": "0901234567", "Email": "nguyenvana@example.com"},
            {"MNV": "E002", "Họ và Tên": "Trần Thị B", "Giới Tính": "Nữ", "Ngày Sinh": "1992-02-15", "Số Điện Thoại": "0912345678", "Email": "tranthib@example.com"},
            {"MNV": "E003", "Họ và Tên": "Lê Văn C", "Giới Tính": "Nam", "Ngày Sinh": "1985-03-20", "Số Điện Thoại": "0923456789", "Email": "levanc@example.com"},
            {"MNV": "E004", "Họ và Tên": "Phạm Thị D", "Giới Tính": "Nữ", "Ngày Sinh": "1995-04-10", "Số Điện Thoại": "0934567890", "Email": "phamthid@example.com"},
            {"MNV": "E005", "Họ và Tên": "Hoàng Văn E", "Giới Tính": "Nam", "Ngày Sinh": "1988-05-25", "Số Điện Thoại": "0945678901", "Email": "hoangvane@example.com"},
        ]
        st.session_state.employees = pd.DataFrame(sample_employees)
    
    # Hiển thị bảng dữ liệu nhân viên
    st.write("### Danh sách nhân viên")
    st.dataframe(st.session_state.employees, use_container_width=True)

    # 🔍 Tìm kiếm nhân viên
    with st.expander("🔍 Tìm kiếm nhân viên"):
        search_query = st.text_input("Nhập từ khóa tìm kiếm:")
        if search_query:
            filtered_df = st.session_state.employees[
                st.session_state.employees.astype(str).apply(
                    lambda row: search_query.lower() in row.to_string().lower(), axis=1
                )
            ]
            st.write("### Kết quả tìm kiếm")
            st.dataframe(filtered_df, use_container_width=True)

    # ➕ Thêm nhân viên
    with st.expander("➕ Thêm nhân viên"):
        with st.form("add_employee_form", clear_on_submit=True):
            employee_id = st.text_input("Mã nhân viên (MNV)")
            full_name = st.text_input("Họ và Tên")
            gender = st.selectbox("Giới Tính", ["Nam", "Nữ", "Khác"])
            birth_date = st.date_input("Ngày Sinh")
            phone = st.text_input("Số Điện Thoại")
            email = st.text_input("Email")
            submitted = st.form_submit_button("Thêm")

            if submitted:
                if employee_id and full_name and phone:
                    # Thêm dữ liệu mới vào DataFrame
                    new_row = {
                        "MNV": employee_id,
                        "Họ và Tên": full_name,
                        "Giới Tính": gender,
                        "Ngày Sinh": birth_date,
                        "Số Điện Thoại": phone,
                        "Email": email
                    }
                    st.session_state.employees = pd.concat(
                        [st.session_state.employees, pd.DataFrame([new_row])],
                        ignore_index=True
                    )
                    st.success("✅ Thêm nhân viên thành công!")
                    st.rerun()
                else:
                    st.error("❌ Vui lòng nhập đầy đủ thông tin bắt buộc!")

    # ✏️ Sửa nhân viên
    with st.expander("✏️ Sửa nhân viên"):
        employee_id_to_edit = st.text_input("Nhập mã nhân viên cần sửa")
        if employee_id_to_edit:
            df = st.session_state.employees
            if employee_id_to_edit in df["MNV"].values:
                row_to_edit = df[df["MNV"] == employee_id_to_edit].iloc[0]
                new_name = st.text_input("Họ và Tên", value=row_to_edit["Họ và Tên"])
                new_gender = st.selectbox("Giới Tính", ["Nam", "Nữ", "Khác"], index=["Nam", "Nữ", "Khác"].index(row_to_edit["Giới Tính"]))
                new_birth_date = st.date_input("Ngày Sinh", value=pd.to_datetime(row_to_edit["Ngày Sinh"]))
                new_phone = st.text_input("Số Điện Thoại", value=row_to_edit["Số Điện Thoại"])
                new_email = st.text_input("Email", value=row_to_edit["Email"])
                if st.button("Cập nhật"):
                    # Cập nhật dữ liệu trong DataFrame
                    st.session_state.employees.loc[
                        df["MNV"] == employee_id_to_edit, ["Họ và Tên", "Giới Tính", "Ngày Sinh", "Số Điện Thoại", "Email"]
                    ] = [new_name, new_gender, new_birth_date, new_phone, new_email]
                    st.success("✅ Cập nhật nhân viên thành công!")
                    st.rerun()
            else:
                st.error("❌ Mã nhân viên không tồn tại!")

    # 🗑️ Xóa nhân viên
    with st.expander("🗑️ Xóa nhân viên"):
        employee_id_to_delete = st.text_input("Nhập mã nhân viên muốn xóa")
        if st.button("Xóa"):
            df = st.session_state.employees
            if employee_id_to_delete in df["MNV"].values:
                # Xóa dữ liệu trong DataFrame
                st.session_state.employees = df[df["MNV"] != employee_id_to_delete]
                st.success(f"✅ Đã xóa nhân viên có mã: {employee_id_to_delete}")
                st.rerun()
            else:
                st.error("❌ Mã nhân viên không tồn tại!")