import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

def show_statistics_tab():
    st.title("📊 Thống kê doanh thu")

    # Khởi tạo dữ liệu bán hàng nếu chưa có
    if "sales_data" not in st.session_state:
        st.session_state.sales_data = pd.DataFrame(columns=[
            "Ngày bán", "Mã hàng", "Tên hàng", "Số lượng đã bán", "Đơn giá", "Doanh số"
        ])
     # Dữ liệu mẫu ban đầu
    if st.session_state.sales_data.empty:
        sample_data = [
            {"Ngày bán": "2025-04-25", "Mã hàng": "P001", "Tên hàng": "iPhone 13", "Số lượng đã bán": 5, "Đơn giá": 20000000, "Doanh số": 100000000},
            {"Ngày bán": "2025-04-24", "Mã hàng": "P002", "Tên hàng": "Samsung S22", "Số lượng đã bán": 3, "Đơn giá": 18000000, "Doanh số": 54000000},
            {"Ngày bán": "2025-04-23", "Mã hàng": "P003", "Tên hàng": "Xiaomi Mi 11", "Số lượng đã bán": 7, "Đơn giá": 15000000, "Doanh số": 105000000},
            {"Ngày bán": "2025-04-22", "Mã hàng": "P004", "Tên hàng": "Oppo Reno 8", "Số lượng đã bán": 4, "Đơn giá": 12000000, "Doanh số": 48000000},
            {"Ngày bán": "2025-04-23", "Mã hàng": "P005", "Tên hàng": "Vivo V23", "Số lượng đã bán": 6, "Đơn giá": 10000000, "Doanh số": 60000000},
            {"Ngày bán": "2025-04-20", "Mã hàng": "P006", "Tên hàng": "Realme GT", "Số lượng đã bán": 8, "Đơn giá": 17000000, "Doanh số": 136000000},
            {"Ngày bán": "2025-03-20", "Mã hàng": "P007", "Tên hàng": "MacBook Air", "Số lượng đã bán": 2, "Đơn giá": 30000000, "Doanh số": 60000000},
            {"Ngày bán": "2025-03-25", "Mã hàng": "P008", "Tên hàng": "Dell XPS 13", "Số lượng đã bán": 3, "Đơn giá": 25000000, "Doanh số": 75000000},
            {"Ngày bán": "2025-02-15", "Mã hàng": "P009", "Tên hàng": "HP Spectre", "Số lượng đã bán": 4, "Đơn giá": 22000000, "Doanh số": 88000000},
            {"Ngày bán": "2025-02-20", "Mã hàng": "P010", "Tên hàng": "Asus ROG", "Số lượng đã bán": 5, "Đơn giá": 35000000, "Doanh số": 175000000},
        ]
        st.session_state.sales_data = pd.DataFrame(sample_data)
    # Hiển thị bảng dữ liệu bán hàng
    st.write("### Danh sách bán hàng")
    if not st.session_state.sales_data.empty:
        # Đảm bảo cột "Ngày bán" là kiểu datetime
        st.session_state.sales_data["Ngày bán"] = pd.to_datetime(
            st.session_state.sales_data["Ngày bán"], errors='coerce'
        )
        # Loại bỏ các hàng có giá trị "Ngày bán" không hợp lệ
        st.session_state.sales_data = st.session_state.sales_data.dropna(subset=["Ngày bán"])
        # Chuyển cột "Ngày bán" sang kiểu chuỗi để hiển thị
        st.session_state.sales_data["Ngày bán"] = st.session_state.sales_data["Ngày bán"].dt.strftime("%Y-%m-%d")
    st.dataframe(st.session_state.sales_data, use_container_width=True)

    # ➕ Thêm dữ liệu bán hàng
    with st.expander("➕ Thêm dữ liệu bán hàng"):
        with st.form("add_sales_form", clear_on_submit=True):
            sale_date = st.date_input("Ngày bán", value=datetime.now())
            product_id = st.text_input("Mã hàng")
            product_name = st.text_input("Tên hàng")
            quantity_sold = st.number_input("Số lượng đã bán", min_value=1, step=1)
            unit_price = st.number_input("Đơn giá", min_value=0.0, step=0.01)
            submitted = st.form_submit_button("Thêm")

            if submitted:
                if product_id and product_name and quantity_sold > 0 and unit_price > 0:
                    # Tính doanh số
                    revenue = quantity_sold * unit_price
                    # Thêm dữ liệu mới vào DataFrame
                    new_row = {
                        "Ngày bán": sale_date,
                        "Mã hàng": product_id,
                        "Tên hàng": product_name,
                        "Số lượng đã bán": quantity_sold,
                        "Đơn giá": unit_price,
                        "Doanh số": revenue
                    }
                    st.session_state.sales_data = pd.concat(
                        [st.session_state.sales_data, pd.DataFrame([new_row])],
                        ignore_index=True
                    )
                    st.success("✅ Thêm dữ liệu bán hàng thành công!")
                    st.rerun()  # Làm mới giao diện
                else:
                    st.error("❌ Vui lòng nhập đầy đủ thông tin hợp lệ!")

    # ✏️ Sửa dữ liệu bán hàng
    with st.expander("✏️ Sửa dữ liệu bán hàng"):
        if not st.session_state.sales_data.empty:
            row_to_edit = st.selectbox("Chọn dòng để sửa", st.session_state.sales_data.index)
            if row_to_edit is not None:
                selected_row = st.session_state.sales_data.loc[row_to_edit]
                sale_date = st.date_input("Ngày bán", value=pd.to_datetime(selected_row["Ngày bán"]))
                product_id = st.text_input("Mã hàng", value=selected_row["Mã hàng"])
                product_name = st.text_input("Tên hàng", value=selected_row["Tên hàng"])
                quantity_sold = st.number_input("Số lượng đã bán", min_value=1, step=1, value=int(selected_row["Số lượng đã bán"]))
                unit_price = st.number_input("Đơn giá", min_value=0.0, step=0.01, value=float(selected_row["Đơn giá"]))
                if st.button("Cập nhật"):
                    # Cập nhật dữ liệu
                    st.session_state.sales_data.loc[row_to_edit] = {
                        "Ngày bán": sale_date,
                        "Mã hàng": product_id,
                        "Tên hàng": product_name,
                        "Số lượng đã bán": quantity_sold,
                        "Đơn giá": unit_price,
                        "Doanh số": quantity_sold * unit_price
                    }
                    st.success("✅ Cập nhật dữ liệu thành công!")
                    st.rerun()

    # 🗑️ Xóa dữ liệu bán hàng
    with st.expander("🗑️ Xóa dữ liệu bán hàng"):
        if not st.session_state.sales_data.empty:
            row_to_delete = st.selectbox("Chọn dòng để xóa", st.session_state.sales_data.index)
            if st.button("Xóa"):
                st.session_state.sales_data = st.session_state.sales_data.drop(index=row_to_delete).reset_index(drop=True)
                st.success("✅ Xóa dữ liệu thành công!")
                st.rerun()

    # 📈 Biểu đồ doanh thu 7 ngày vừa qua
    st.write("### 📈 Doanh thu 7 ngày vừa qua")
    today = datetime.now()
    last_7_days = today - timedelta(days=7)

    if not st.session_state.sales_data.empty:
        # Đảm bảo cột "Ngày bán" là kiểu datetime
        st.session_state.sales_data["Ngày bán"] = pd.to_datetime(
            st.session_state.sales_data["Ngày bán"], errors='coerce'
        )
        # Lọc dữ liệu bán hàng trong 7 ngày vừa qua
        recent_sales = st.session_state.sales_data[
            (st.session_state.sales_data["Ngày bán"] >= last_7_days) &
            (st.session_state.sales_data["Ngày bán"] <= today)
        ]
        if not recent_sales.empty:
            # Nhóm dữ liệu theo ngày và tính tổng doanh số
            daily_revenue = recent_sales.groupby(recent_sales["Ngày bán"].dt.date)["Doanh số"].sum().reset_index()
            daily_revenue.columns = ["Ngày", "Doanh số"]
            # Vẽ biểu đồ
            fig_7_days = px.bar(
                daily_revenue,
                x="Ngày",
                y="Doanh số",
                title="Doanh thu 7 ngày vừa qua",
                labels={"Doanh số": "VNĐ", "Ngày": "Ngày"},
                text="Doanh số"
            )
            fig_7_days.update_traces(texttemplate='%{text:.2s}', textposition='outside')
            st.plotly_chart(fig_7_days, use_container_width=True)
        else:
            st.info("Không có doanh thu trong 7 ngày vừa qua.")

    # 📊 Biểu đồ doanh thu theo tháng
    st.write("### 📊 Doanh thu theo tháng")
    if not st.session_state.sales_data.empty:
        # Đảm bảo cột "Ngày bán" là kiểu datetime
        st.session_state.sales_data["Ngày bán"] = pd.to_datetime(
            st.session_state.sales_data["Ngày bán"], errors='coerce'
        )
        # Loại bỏ các giá trị không hợp lệ
        valid_sales_data = st.session_state.sales_data.dropna(subset=["Ngày bán"])
        if not valid_sales_data.empty:
            # Nhóm dữ liệu theo tháng và tính tổng doanh số
            monthly_revenue = valid_sales_data.groupby(
                valid_sales_data["Ngày bán"].dt.to_period("M")
            )["Doanh số"].sum().reset_index()
            monthly_revenue["Tháng"] = monthly_revenue["Ngày bán"].astype(str)
            monthly_revenue = monthly_revenue[["Tháng", "Doanh số"]]
            # Vẽ biểu đồ cột
            fig_monthly = px.bar(
                monthly_revenue,
                x="Tháng",
                y="Doanh số",
                title="Doanh thu theo tháng",
                labels={"Doanh số": "VNĐ", "Tháng": "Tháng"},
                text="Doanh số"
            )
            fig_monthly.update_traces(texttemplate='%{text:.2s}', textposition='outside')
            st.plotly_chart(fig_monthly, use_container_width=True)
        else:
            st.info("Không có dữ liệu doanh thu hợp lệ để hiển thị.")
    else:
        st.info("Không có dữ liệu doanh thu theo tháng.")