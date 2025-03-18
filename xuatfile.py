import pandas as pd
import streamlit as st

# Hàm đọc dữ liệu từ Excel
def get_data_from_excel():
    df = pd.read_excel(
        io="C:\\Users\\tranp\\OneDrive\\Desktop\\vscode\\.vscode\\nuedu-622076703652257.xlsx",
        engine="openpyxl",
        sheet_name=0,   # Chọn sheet đầu tiên (có thể đổi nếu cần)
        usecols="A:G",  # Đọc từ cột A đến G
        nrows=123       # Giới hạn số dòng đọc
    )
    
    # Chuẩn hóa tên cột để tránh lỗi chính tả/khoảng trắng ẩn
    df.columns = df.columns.str.strip().str.lower()

    # Đổi tên cột A và C cho dễ đọc
    df.rename(columns={"a": "uid", "c": "dien_thoai"}, inplace=True)

    return df

# Đọc dữ liệu
df = get_data_from_excel()

# Hiển thị tên cột để kiểm tra
print("Các cột trong DataFrame:", df.columns)

# Cấu hình Streamlit
st.set_page_config(page_title="Báo cáo số", page_icon="🤑")
st.sidebar.header("Lọc dữ liệu tại đây")

# Tạo bộ lọc trên sidebar
if "uid" in df.columns and "dien_thoai" in df.columns:
    selected_uids = st.sidebar.multiselect("Chọn UID", options=df["uid"].astype(str).unique())
    selected_phones = st.sidebar.multiselect("Chọn số điện thoại", options=df["dien_thoai"].astype(str).unique())

    # Lọc dữ liệu theo UID & SĐT
    filtered_df = df.copy()
    if selected_uids:
        filtered_df = filtered_df[filtered_df["uid"].astype(str).isin(selected_uids)]
    if selected_phones:
        filtered_df = filtered_df[filtered_df["dien_thoai"].astype(str).isin(selected_phones)]

    # Hiển thị kết quả
    st.write("### Dữ liệu đã lọc:")
    st.dataframe(filtered_df)
else:
    st.sidebar.error("Không tìm thấy cột 'UID' hoặc 'Số điện thoại' trong file Excel!")
