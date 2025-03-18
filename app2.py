import streamlit as st

# Tạo danh sách tài khoản mẫu
USER_CREDENTIALS = {
    "admin": "123456",
    "user": "password"
}

# Hàm kiểm tra đăng nhập
def check_login(username, password):
    return USER_CREDENTIALS.get(username) == password

# Thiết lập giao diện
st.set_page_config(page_title="Đăng nhập", page_icon="🔑")

st.title("🔑 Đăng nhập vào hệ thống")

# Tạo form đăng nhập
with st.form("login_form"):
    username = st.text_input("👤 Tên đăng nhập")
    password = st.text_input("🔒 Mật khẩu", type="password")
    submit = st.form_submit_button("Đăng nhập")

# Xử lý đăng nhập
if submit:
    if check_login(username, password):
        st.success(f"✅ Đăng nhập thành công! Chào mừng, **{username}** 🎉")
    else:
        st.error("❌ Sai tên đăng nhập hoặc mật khẩu. Vui lòng thử lại!")

# Thêm thông tin liên hệ
st.markdown("---")
st.info("📧 Liên hệ hỗ trợ: support@example.com")
