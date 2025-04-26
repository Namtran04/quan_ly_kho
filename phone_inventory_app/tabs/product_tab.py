import streamlit as st
import pandas as pd

def show_products_tab():
    st.title("📦 Danh sách sản phẩm trong kho")
    # Khởi tạo dữ liệu sản phẩm nếu chưa có
    if "products" not in st.session_state:
        st.session_state.products = pd.DataFrame(columns=[
            "Mã hàng", "Tên hàng", "Số lượng", "Đơn giá", "Bộ xử lý", "RAM", "Bộ nhớ"
        ])

    # Dữ liệu mẫu ban đầu
    if st.session_state.products.empty:
        sample_products = [
            {"Mã hàng": "P001", "Tên hàng": "iPhone 13", "Số lượng": 50, "Đơn giá": 20000000, "Bộ xử lý": "A15 Bionic", "RAM": "4GB", "Bộ nhớ": "128GB"},
            {"Mã hàng": "P002", "Tên hàng": "Samsung S22", "Số lượng": 30, "Đơn giá": 18000000, "Bộ xử lý": "Exynos 2200", "RAM": "8GB", "Bộ nhớ": "256GB"},
            {"Mã hàng": "P003", "Tên hàng": "Xiaomi Mi 11", "Số lượng": 70, "Đơn giá": 15000000, "Bộ xử lý": "Snapdragon 888", "RAM": "8GB", "Bộ nhớ": "128GB"},
            {"Mã hàng": "P004", "Tên hàng": "Oppo Reno 8", "Số lượng": 40, "Đơn giá": 12000000, "Bộ xử lý": "Dimensity 8100", "RAM": "8GB", "Bộ nhớ": "256GB"},
            {"Mã hàng": "P005", "Tên hàng": "Vivo V23", "Số lượng": 60, "Đơn giá": 10000000, "Bộ xử lý": "Dimensity 920", "RAM": "8GB", "Bộ nhớ": "128GB"},
            {"Mã hàng": "P006", "Tên hàng": "Realme GT", "Số lượng": 80, "Đơn giá": 17000000, "Bộ xử lý": "Snapdragon 870", "RAM": "12GB", "Bộ nhớ": "256GB"},
            {"Mã hàng": "P007", "Tên hàng": "MacBook Air", "Số lượng": 20, "Đơn giá": 30000000, "Bộ xử lý": "M1", "RAM": "8GB", "Bộ nhớ": "256GB"},
            {"Mã hàng": "P008", "Tên hàng": "Dell XPS 13", "Số lượng": 25, "Đơn giá": 25000000, "Bộ xử lý": "Intel i7", "RAM": "16GB", "Bộ nhớ": "512GB"},
            {"Mã hàng": "P009", "Tên hàng": "HP Spectre", "Số lượng": 35, "Đơn giá": 22000000, "Bộ xử lý": "Intel i5", "RAM": "8GB", "Bộ nhớ": "256GB"},
            {"Mã hàng": "P010", "Tên hàng": "Asus ROG", "Số lượng": 15, "Đơn giá": 35000000, "Bộ xử lý": "Ryzen 9", "RAM": "16GB", "Bộ nhớ": "1TB"},
        ]
        st.session_state.products = pd.DataFrame(sample_products)
    st.dataframe(st.session_state.products, use_container_width=True, height=300)

    # 🔍 Tìm kiếm sản phẩm
    with st.expander("🔍 Tìm kiếm sản phẩm"):
        search_query = st.text_input("Nhập từ khóa tìm kiếm:")
        if search_query:
            filtered_df = st.session_state.products[
                st.session_state.products.astype(str).apply(
                    lambda row: search_query.lower() in row.to_string().lower(), axis=1
                )
            ]
            st.dataframe(filtered_df, use_container_width=True)

    # ➕ Thêm sản phẩm
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
                new_product = {
                    "Mã hàng": ma_hang,
                    "Tên hàng": ten_hang,
                    "Số lượng": so_luong,
                    "Đơn giá": don_gia,
                    "Bộ xử lý": bo_xu_ly,
                    "RAM": ram,
                    "Bộ nhớ": bo_nho,
                }
                st.session_state.products = pd.concat(
                    [st.session_state.products, pd.DataFrame([new_product])],
                    ignore_index=True,
                )
                st.success("✅ Đã thêm sản phẩm mới!")
                st.rerun()

    # ✏️ Sửa sản phẩm
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
                    st.session_state.products.loc[
                        df["Mã hàng"] == ma_hang_sua,
                        ["Tên hàng", "Số lượng", "Đơn giá", "Bộ xử lý", "RAM", "Bộ nhớ"]
                    ] = [ten_hang, so_luong, don_gia, bo_xu_ly, ram, bo_nho]
                    st.success("✅ Cập nhật sản phẩm thành công!")
                    st.rerun()
            else:
                st.error("❌ Mã hàng không tồn tại!")

    # 🗑️ Xóa sản phẩm
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
