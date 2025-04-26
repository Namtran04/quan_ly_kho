import streamlit as st

def show_home_tab():
    st.title("Hệ thống quản lý kho điện thoại theo mã IMEI")
    st.markdown("""
    ### - Hãy hướng về phía mặt trời, nơi mà bóng tối luôn ở phía sau lưng bạn. Điều mà hoa hướng dương vẫn làm mỗi ngày. -
    #### Tập đoàn AnBaChSi
    """)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/accuracy.png", use_column_width=True)
        st.subheader("Tính chính xác")
        st.write("Mã IMEI là một số duy nhất được gắn cho từng thiết bị điện thoại, giúp đảm bảo tính chính xác và độ tin cậy cao.")

    with col2:
        st.image("assets/security.png", use_column_width=True)
        st.subheader("Tính bảo mật")
        st.write("Ngăn chặn việc sử dụng các thiết bị giả mạo hoặc bị đánh cắp, tăng tính bảo mật cho hoạt động quản lý.")

    with col3:
        st.image("assets/efficiency.png", use_column_width=True)
        st.subheader("Tính hiệu quả")
        st.write("Dễ dàng xác định thông tin về từng thiết bị điện thoại một cách nhanh chóng và chính xác.")