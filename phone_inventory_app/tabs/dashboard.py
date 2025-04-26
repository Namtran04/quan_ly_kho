import streamlit as st
from tabs import product_tab, export_tab, import_tab

def show_dashboard_tab():
    # CSS tùy chỉnh
    dashboard_css = """
    <style>
        body {
            background-color: #f7f9fc;
        }
        .dashboard-container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .dashboard-header {
            text-align: center;
            margin-bottom: 30px;
        }
        .dashboard-header h1 {
            font-size: 2.5rem;
            color: #333333;
        }
        .dashboard-header p {
            font-size: 1.2rem;
            color: #555555;
        }
        .card-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 20px;
        }
        .card {
            flex: 1 1 calc(33.333% - 20px);
            max-width: calc(33.333% - 20px);
            background: #007bff;
            color: white;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        }
        .card img {
            max-width: 50px;
            margin-bottom: 10px;
        }
        .card h3 {
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        .card p {
            font-size: 1rem;
        }
    </style>
    """

    # HTML giao diện
    dashboard_html = """
    <div class="dashboard-container">
        <div class="dashboard-header">
            <h1>📊 Quản lý kho hàng</h1>
            <p>Chào mừng bạn đến với hệ thống quản lý kho hàng hiện đại!</p>
        </div>
        <div class="card-container">
            <div class="card" onclick="window.location.href='/#📦Sản phẩm'">
                <img src="https://img.icons8.com/color/96/000000/box.png" alt="Sản phẩm">
                <h3>Quản lý Sản phẩm</h3>
                <p>Thêm, sửa, xóa và quản lý danh sách sản phẩm trong kho.</p>
            </div>
            <div class="card" onclick="window.location.href='/#📤Xuất Excel'">
                <img src="https://img.icons8.com/color/96/000000/export.png" alt="Xuất Excel">
                <h3>Xuất Excel</h3>
                <p>Xuất dữ liệu kho hàng ra file Excel.</p>
            </div>
            <div class="card" onclick="window.location.href='/#📥Nhập Excel'">
                <img src="https://img.icons8.com/color/96/000000/import.png" alt="Nhập Excel">
                <h3>Nhập Excel</h3>
                <p>Nhập dữ liệu từ file Excel vào hệ thống.</p>
            </div>
        </div>
    </div>
    """

    # Hiển thị CSS và HTML
    st.markdown(dashboard_css, unsafe_allow_html=True)
    st.markdown(dashboard_html, unsafe_allow_html=True)

    # Sidebar
    st.sidebar.header(f"👋 Xin chào, {st.session_state.username}!")
    menu = ["📦Sản phẩm", "📤Xuất Excel", "📥Nhập Excel", "🚪Đăng xuất"]
    choice = st.sidebar.radio("Chức năng", menu)

    # Điều hướng sidebar
    if choice == "📦Sản phẩm":
        product_tab.show_products_tab()
    elif choice == "📤Xuất Excel":
        export_tab.show_export_tab()
    elif choice == "📥Nhập Excel":
        import_tab.show_import_tab()
    elif choice == "🚪Đăng xuất":
        st.session_state.logged_in = False
        st.experimental_rerun()