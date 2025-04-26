import bcrypt
import mysql.connector
from utils.database import get_connection

def validate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    conn.close()

    # So sánh trực tiếp mật khẩu gốc
    if user and user['password'] == password:
        return user
    return None

def register_user(username, password, role="user"):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (username, password, role))  # Lưu mật khẩu gốc
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        conn.close()