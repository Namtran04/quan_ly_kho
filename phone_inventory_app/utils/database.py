import mysql.connector

# Hàm kết nối đến MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",       # Địa chỉ MySQL (thường là localhost)
        user="root",            # Tên người dùng MySQL
        password="123456",# Mật khẩu MySQL
        database="phone_inventory"  # Tên cơ sở dữ liệu
    )

