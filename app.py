import streamlit as st
import pandas as pd

# Thiết lập cấu hình trang web
st.set_page_config(page_title="Phần mềm quản lý kho", page_icon="📦", layout="wide")

# Tạo danh sách tài khoản mẫu
USER_CREDENTIALS = {
    "admin": "123456",
    "user": "password"
}

# Kiểm tra xem đã đăng nhập chưa
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Nếu chưa đăng nhập -> Hiển thị giao diện Login
if not st.session_state.logged_in:
    st.markdown(
        """
        <style>
            .container {
                display: flex;
            }
            .left {
                width: 40%;
                background-color: #4CAF50;
                padding: 50px;
                color: white;
                font-size: 30px;
                text-align: center;
            }
            .right {
                width: 60%;
                background-color: #1E293B;
                padding: 50px;
                color: white;
            }
            input {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
            }
            button {
                width: 100%;
                padding: 10px;
                background-color: #4CAF50;
                border: none;
                color: white;
                font-size: 18px;
                cursor: pointer;
            }
        </style>
        <div class="container">
            <div class="left">
                <h1>LOGIN</h1>
            </div>
            <div class="right">
                <h2>Đăng nhập vào phần mềm</h2>
        """,
        unsafe_allow_html=True
    )

    username = st.text_input("👤 Tên đăng nhập")
    password = st.text_input("🔒 Mật khẩu", type="password")
    login_btn = st.button("Đăng nhập")

    if login_btn:
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("❌ Sai tên đăng nhập hoặc mật khẩu. Vui lòng thử lại!")

# Nếu đã đăng nhập -> Hiển thị giao diện quản lý kho hàng
else:
    st.sidebar.header(f"👋 Xin chào, {st.session_state.username}!")
    
    # Giao diện thanh công cụ
    st.sidebar.header("📂 Quản lý kho hàng")
    menu = ["Sản phẩm", "Xuất Excel", "Nhập Excel", "Đăng xuất"]
    choice = st.sidebar.radio("Chọn chức năng", menu)

    # Khởi tạo dữ liệu sản phẩm nếu chưa có
    if "products" not in st.session_state:
        st.session_state.products = pd.DataFrame([
            {"Mã hàng": "LP13", "Tên hàng": "Laptop HP", "Số lượng": 19, "Đơn giá": "9.990.000đ", "Bộ xử lý": "Intel Core i3", "RAM": "4GB", "Bộ nhớ": "256GB"},
            {"Mã hàng": "LP14", "Tên hàng": "Laptop Lenovo", "Số lượng": 3, "Đơn giá": "22.490.000đ", "Bộ xử lý": "Intel Core i5", "RAM": "8GB", "Bộ nhớ": "512GB"},
            {"Mã hàng": "LP15", "Tên hàng": "Laptop Acer", "Số lượng": 62, "Đơn giá": "22.990.000đ", "Bộ xử lý": "Intel Core i7", "RAM": "16GB", "Bộ nhớ": "1TB"}
        ])

    # Chức năng quản lý sản phẩm
    if choice == "Sản phẩm":
        st.title("📦 Danh sách sản phẩm trong kho")

        df = st.session_state.products
        st.dataframe(df)

        # Giao diện chức năng
        col1, col2 = st.columns([3, 2])

        # Cột 1: Chức năng quản lý sản phẩm
        with col1:
            st.subheader("🔧 Chức năng")
            col_a, col_b, col_c, col_d, col_e, col_f = st.columns(6)

            if col_a.button("➕ Thêm"):
                with st.form("Thêm sản phẩm"):
                    ma_hang = st.text_input("Mã hàng")
                    ten_hang = st.text_input("Tên hàng")
                    so_luong = st.number_input("Số lượng", min_value=1)
                    don_gia = st.text_input("Đơn giá")
                    bo_xu_ly = st.text_input("Bộ xử lý")
                    ram = st.text_input("RAM")
                    bo_nho = st.text_input("Bộ nhớ")
                    submit_add = st.form_submit_button("Xác nhận")

                    if submit_add:
                        new_product = {"Mã hàng": ma_hang, "Tên hàng": ten_hang, "Số lượng": so_luong, "Đơn giá": don_gia, "Bộ xử lý": bo_xu_ly, "RAM": ram, "Bộ nhớ": bo_nho}
                        st.session_state.products = pd.concat([st.session_state.products, pd.DataFrame([new_product])], ignore_index=True)
                        st.success("✅ Đã thêm sản phẩm mới!")
                        st.rerun()

            selected_product = st.selectbox("🔍 Chọn sản phẩm để chỉnh sửa:", df["Mã hàng"])

            # Sửa sản phẩm
            if col_b.button("✏️ Sửa"):
                product_data = df[df["Mã hàng"] == selected_product].iloc[0]
                with st.form("Sửa sản phẩm"):
                    ten_hang = st.text_input("Tên hàng", product_data["Tên hàng"])
                    so_luong = st.number_input("Số lượng", min_value=1, value=int(product_data["Số lượng"]))
                    don_gia = st.text_input("Đơn giá", product_data["Đơn giá"])
                    bo_xu_ly = st.text_input("Bộ xử lý", product_data["Bộ xử lý"])
                    ram = st.text_input("RAM", product_data["RAM"])
                    bo_nho = st.text_input("Bộ nhớ", product_data["Bộ nhớ"])
                    submit_edit = st.form_submit_button("Xác nhận")

                    if submit_edit:
                        index = df[df["Mã hàng"] == selected_product].index[0]
                        st.session_state.products.loc[index] = {"Mã hàng": selected_product, "Tên hàng": ten_hang, "Số lượng": so_luong, "Đơn giá": don_gia, "Bộ xử lý": bo_xu_ly, "RAM": ram, "Bộ nhớ": bo_nho}
                        st.success("✅ Cập nhật sản phẩm thành công!")
                        st.rerun()

            # Xóa sản phẩm
            if col_c.button("🗑️ Xóa"):
                st.session_state.products = df[df["Mã hàng"] != selected_product]
                st.warning("🗑️ Đã xóa sản phẩm!")
                st.rerun()

            # Xem chi tiết sản phẩm
            if col_d.button("🔍 Xem chi tiết"):
                st.json(df[df["Mã hàng"] == selected_product].iloc[0].to_dict())

            # Xuất Excel
            if col_e.button("📤 Xuất Excel"):
                @st.cache_data
                def convert_df(df):
                    return df.to_csv(index=False).encode('utf-8')

                csv = convert_df(st.session_state.products)
                st.download_button(label="📥 Tải file Excel", data=csv, file_name="kho_hang.csv", mime="text/csv")
                st.success("✅ Xuất file thành công!")

            # Nhập Excel
            if col_f.button("📥 Nhập Excel"):
                uploaded_file = st.file_uploader("📂 Chọn file Excel", type=["csv"])
                if uploaded_file is not None:
                    df_new = pd.read_csv(uploaded_file)
                    st.session_state.products = pd.concat([st.session_state.products, df_new], ignore_index=True)
                    st.success("✅ Dữ liệu đã được nhập!")
                    st.rerun()

        # Cột 2: Tìm kiếm
        with col2:
            st.subheader("🔎 Tìm kiếm sản phẩm")
            filter_col = st.selectbox("🔄 Lọc theo:", ["Tất cả", "Mã hàng", "Tên hàng"])
            search_query = st.text_input("🔍 Nhập từ khóa tìm kiếm:")

            if search_query:
                if filter_col == "Tất cả":
                    filtered_df = df[df.apply(lambda row: search_query.lower() in row.astype(str).str.lower().to_string(), axis=1)]
                else:
                    filtered_df = df[df[filter_col].astype(str).str.contains(search_query, case=False, na=False)]

                st.dataframe(filtered_df)

            if st.button("🔄 Làm mới"):
                st.rerun()

    # Xuất Excel
    elif choice == "Xuất Excel":
        st.title("📤 Xuất danh sách sản phẩm ra Excel")
        csv = st.session_state.products.to_csv(index=False).encode('utf-8')
        st.download_button(label="📥 Tải file Excel", data=csv, file_name="kho_hang.csv", mime="text/csv")

    # Nhập Excel
    elif choice == "Nhập Excel":
        st.title("📥 Nhập danh sách sản phẩm từ Excel")
        uploaded_file = st.file_uploader("📂 Chọn file Excel", type=["csv"])
        if uploaded_file is not None:
            df_new = pd.read_csv(uploaded_file)
            st.session_state.products = pd.concat([st.session_state.products, df_new], ignore_index=True)
            st.success("✅ Dữ liệu đã được nhập!")
            st.rerun()

    # Đăng xuất
    elif choice == "Đăng xuất":
        st.session_state.logged_in = False
        st.rerun()

# Footer
st.markdown("---")
st.info("📧 Hỗ trợ: support@example.com")