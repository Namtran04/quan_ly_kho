import streamlit as st
import pandas as pd

# Cấu hình trang web
st.set_page_config(page_title="Quản lý kho", page_icon="📦", layout="wide")

# Danh sách tài khoản
USER_CREDENTIALS = {"admin": "123456", "user": "password"}

# Kiểm tra đăng nhập
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
    menu = ["Sản phẩm", "Xuất Excel", "Nhập Excel", "Đăng xuất"]
    choice = st.sidebar.radio("Chức năng", menu)

    # Dữ liệu sản phẩm
    if "products" not in st.session_state:
        st.session_state.products = pd.DataFrame(columns=["Mã hàng", "Tên hàng", "Số lượng", "Đơn giá", "Bộ xử lý", "RAM", "Bộ nhớ"])
    
    if choice == "Sản phẩm":
        st.title("📦 Danh sách sản phẩm trong kho")
        st.dataframe(st.session_state.products, use_container_width=True, height=300)

        with st.expander("🔍 Tìm kiếm sản phẩm"):
            search_query = st.text_input("Nhập từ khóa tìm kiếm:")
            filtered_df = st.session_state.products[st.session_state.products.astype(str).apply(lambda row: search_query.lower() in row.to_string().lower(), axis=1)]
            st.dataframe(filtered_df, use_container_width=True)
        
        with st.expander("➕ Thêm sản phẩm"):
            with st.form("add_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with col1:
                    ma_hang = st.text_input("Mã hàng")
                    ten_hang = st.text_input("Tên hàng")
                    so_luong = st.number_input("Số lượng", min_value=1)
                with col2:
                    don_gia = st.text_input("Đơn giá")
                    bo_xu_ly = st.text_input("Bộ xử lý")
                    ram = st.text_input("RAM")
                    bo_nho = st.text_input("Bộ nhớ")
                submit_add = st.form_submit_button("Thêm sản phẩm")
                if submit_add:
                    new_product = {"Mã hàng": ma_hang, "Tên hàng": ten_hang, "Số lượng": so_luong, "Đơn giá": don_gia, "Bộ xử lý": bo_xu_ly, "RAM": ram, "Bộ nhớ": bo_nho}
                    st.session_state.products = pd.concat([st.session_state.products, pd.DataFrame([new_product])], ignore_index=True)
                    st.success("✅ Đã thêm sản phẩm mới!")
                    st.rerun()
        
        with st.expander("✏️ Sửa sản phẩm"):
            ma_hang_sua = st.text_input("Nhập mã hàng cần sửa")
            if ma_hang_sua:
                df = st.session_state.products
                if ma_hang_sua in df["Mã hàng"].values:
                    product = df[df["Mã hàng"] == ma_hang_sua].iloc[0]
                    ten_hang = st.text_input("Tên hàng", value=product["Tên hàng"])
                    so_luong = st.number_input("Số lượng", min_value=1, value=int(product["Số lượng"]))
                    don_gia = st.text_input("Đơn giá", value=product["Đơn giá"])
                    bo_xu_ly = st.text_input("Bộ xử lý", value=product["Bộ xử lý"])
                    ram = st.text_input("RAM", value=product["RAM"])
                    bo_nho = st.text_input("Bộ nhớ", value=product["Bộ nhớ"])
                    if st.button("Cập nhật"):
                        st.session_state.products.loc[df["Mã hàng"] == ma_hang_sua, ["Tên hàng", "Số lượng", "Đơn giá", "Bộ xử lý", "RAM", "Bộ nhớ"]] = [ten_hang, so_luong, don_gia, bo_xu_ly, ram, bo_nho]
                        st.success("✅ Cập nhật sản phẩm thành công!")
                        st.rerun()
                else:
                    st.error("❌ Mã hàng không tồn tại!")
        
        with st.expander("🗑️ Xóa sản phẩm"):
            ma_hang_xoa = st.text_input("Nhập mã hàng muốn xóa")
            if st.button("Xóa"):
                df = st.session_state.products
                if ma_hang_xoa in df["Mã hàng"].values:
                    st.session_state.products = df[df["Mã hàng"] != ma_hang_xoa]
                    st.success(f"✅ Đã xóa sản phẩm có mã hàng: {ma_hang_xoa}")
                    st.rerun()
                else:
                    st.error("❌ Mã hàng không tồn tại!")
    
    elif choice == "Xuất Excel":
        st.title("📤 Xuất danh sách sản phẩm")
        st.download_button(label="📥 Tải file", data=st.session_state.products.to_csv(index=False).encode('utf-8'), file_name="kho_hang.csv", mime="text/csv")
    
    elif choice == "Nhập Excel":
        st.title("📥 Nhập dữ liệu từ Excel")
        uploaded_file = st.file_uploader("📂 Chọn file", type=["xlsx"])
        if uploaded_file:
            df_new = pd.read_excel(uploaded_file, engine='openpyxl')
            st.session_state.products = pd.concat([st.session_state.products, df_new], ignore_index=True)
            st.success("✅ Dữ liệu đã được nhập!")
            st.rerun()
    
    elif choice == "Đăng xuất":
        st.session_state.logged_in = False
        st.rerun()
