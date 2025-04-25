import streamlit as st
import pandas as pd

# Import các tab
from tabs.login_tab import show_login_tab
from tabs.dashboard import show_dashboard_tab
from tabs.product_tab import show_products_tab
from tabs.import_tab import show_import_tab
from tabs.export_tab import show_export_tab
from tabs.warehouse_tab import show_warehouse_tab
from tabs.supplier_tab import show_supplier_tab
from tabs.employee_tab import show_employee_tab
from tabs.account_tab import show_account_tab
from tabs.statistics_tab import show_statistics_tab
from tabs.customer_tab import show_customer_tab

# Khởi tạo dữ liệu session mặc định
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if "current_tab" not in st.session_state:
    st.session_state.current_tab = "🏠 Trang chủ"  # Tab mặc định


# Giao diện chính
def main():
    st.set_page_config(page_title="📱 Quản lý kho điện thoại", layout="wide")

    if not st.session_state.is_logged_in:
        show_login_tab()
    else:
        # Sidebar với các chức năng
        st.sidebar.title("Hệ thống quản lý kho hàng")
        st.sidebar.subheader("Trần Phương Nam")
        st.sidebar.write("Quản lý kho")

        # Các nút điều hướng
        if st.sidebar.button("🏠 Trang chủ"):
            st.session_state.current_tab = "🏠 Trang chủ"
        if st.sidebar.button("📦 Sản phẩm"):
            st.session_state.current_tab = "📦 Sản phẩm"
        if st.sidebar.button("📝 Thuộc tính"):
            st.session_state.current_tab = "📝 Thuộc tính"
        if st.sidebar.button("📍 Khu vực kho"):
            st.session_state.current_tab = "📍 Khu vực kho"
        if st.sidebar.button("📥 Phiếu nhập"):
            st.session_state.current_tab = "📥 Phiếu nhập"
        if st.sidebar.button("📤 Phiếu xuất"):
            st.session_state.current_tab = "📤 Phiếu xuất"
        if st.sidebar.button("👥 Khách hàng"):
            st.session_state.current_tab = "👥 Khách hàng"
        if st.sidebar.button("🏢 Nhà cung cấp"):
            st.session_state.current_tab = "🏢 Nhà cung cấp"
        if st.sidebar.button("👨‍💼 Nhân viên"):
            st.session_state.current_tab = "👨‍💼 Nhân viên"
        if st.sidebar.button("🔑 Tài khoản"):
            st.session_state.current_tab = "🔑 Tài khoản"
        if st.sidebar.button("📊 Thống kê"):
            st.session_state.current_tab = "📊 Thống kê"
        if st.sidebar.button("⚙️ Phân quyền"):
            st.session_state.current_tab = "⚙️ Phân quyền"
        if st.sidebar.button("🚪 Đăng xuất"):
            st.session_state.is_logged_in = False
            st.success("Đã đăng xuất!")

        # Hiển thị nội dung tương ứng với tab hiện tại
        if st.session_state.current_tab == "🏠 Trang chủ":
            show_dashboard_tab()
        elif st.session_state.current_tab == "📦 Sản phẩm":
            show_products_tab()
        elif st.session_state.current_tab == "📝 Thuộc tính":
            st.write("Thuộc tính - Đang phát triển...")
        elif st.session_state.current_tab == "📍 Khu vực kho":
            show_warehouse_tab()
        elif st.session_state.current_tab == "📥 Phiếu nhập":
            show_import_tab()
        elif st.session_state.current_tab == "📤 Phiếu xuất":
            show_export_tab()
        elif st.session_state.current_tab == "👥 Khách hàng":
            show_customer_tab()
        elif st.session_state.current_tab == "🏢 Nhà cung cấp":
            show_supplier_tab()
        elif st.session_state.current_tab == "👨‍💼 Nhân viên":
            show_employee_tab()
        elif st.session_state.current_tab == "🔑 Tài khoản":
            show_account_tab()
        elif st.session_state.current_tab == "📊 Thống kê":
            show_statistics_tab()
        elif st.session_state.current_tab == "⚙️ Phân quyền":
            st.write("Phân quyền - Đang phát triển...")

# Chạy app
if __name__ == "__main__":
    main()