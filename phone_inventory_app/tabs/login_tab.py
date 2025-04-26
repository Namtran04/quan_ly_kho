import streamlit as st
from utils.db_handler import validate_user, register_user

def show_login_tab():
    st.title("Đăng nhập hoặc Đăng ký")

    # Tabs cho Đăng nhập và Đăng ký
    tab = st.radio("Chọn chức năng", ["Đăng nhập", "Đăng ký"])

    if tab == "Đăng nhập":
        # Giao diện đăng nhập
        username = st.text_input("Tên đăng nhập")
        password = st.text_input("Mật khẩu", type="password")

        if st.button("Đăng nhập"):
            user = validate_user(username, password)
            if user:
                st.session_state.is_logged_in = True
                st.session_state.username = user["username"]
                st.session_state.role = user["role"]
                st.success(f"Đăng nhập thành công! Xin chào, {user['username']}.")
                st.rerun()
            else:
                st.error("Tên đăng nhập hoặc mật khẩu không đúng!")

    elif tab == "Đăng ký":
        # Giao diện đăng ký
        new_username = st.text_input("Tên đăng nhập mới")
        new_password = st.text_input("Mật khẩu mới", type="password")
        confirm_password = st.text_input("Xác nhận mật khẩu", type="password")

        if st.button("Đăng ký"):
            if new_password != confirm_password:
                st.error("Mật khẩu xác nhận không khớp!")
            elif len(new_password) < 6:
                st.error("Mật khẩu phải có ít nhất 6 ký tự!")
            else:
                success = register_user(new_username, new_password)
                if success:
                    st.success("Đăng ký thành công! Bạn có thể đăng nhập ngay bây giờ.")
                    
                else:
                    st.error("Tên đăng nhập đã tồn tại. Vui lòng chọn tên khác.")











# import streamlit as st

# def show_login_tab():
#     USER_CREDENTIALS = {
#         "admin": "123456",  # Bạn có thể thêm nhiều tài khoản khác nếu muốn
#     }

#     st.markdown(
#         """
#         <style>
#             .container { display: flex; flex-direction: row; }
#             .left {
#                 width: 40%; background-color: #4CAF50; padding: 50px;
#                 color: white; font-size: 30px; text-align: center;
#             }
#             .right {
#                 width: 60%; background-color: #1E293B; padding: 50px;
#                 color: white;
#             }
#         </style>
#         <div class="container">
#             <div class="left"><h1>LOGIN</h1></div>
#             <div class="right"><h2>Đăng nhập vào phần mềm</h2>
#         """,
#         unsafe_allow_html=True
#     )

#     username = st.text_input("👤 Tên đăng nhập")
#     password = st.text_input("🔒 Mật khẩu", type="password")
#     login_btn = st.button("Đăng nhập")

#     if login_btn:
#         if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
#             st.session_state.is_logged_in = True
#             st.session_state.username = username
#             st.success("✅ Đăng nhập thành công!")
#             st.rerun()
#         else:
#             st.error("❌ Sai tên đăng nhập hoặc mật khẩu. Vui lòng thử lại!")
