import json
import os

class Product:
    def __init__(self, pid, name, quantity, price):
        self.id = pid
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

    @staticmethod
    def from_dict(data):
        return Product(data['id'], data['name'], data['quantity'], data['price'])

class Warehouse:
    def __init__(self, filename='kho.json'):
        self.filename = filename
        self.products = {}  

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Product.from_dict(p) for p in data]
        return []

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([p.to_dict() for p in self.products], f, indent=4, ensure_ascii=False)

    def exists(self, pid):
        return any(p.id == pid for p in self.products)

    def add_product(self, pid, name, quantity, price):
        if self.exists(pid):
            print("\nID đã tồn tại. Không thể thêm sản phẩm!")
            return
        self.products.append(Product(pid, name, quantity, price))
        print("\nSản phẩm đã được thêm vào kho!")

    def display_products(self):
        if not self.products:
            print("\nKho hàng đang trống!")
            return
        print("\nDanh sách sản phẩm trong kho:\n")
        print(f"{'ID':<5}{'Tên':<20}{'Số lượng':<12}{'Giá':<10}")
        print("-" * 45)
        for p in self.products:
            print(f"{p.id:<5}{p.name:<20}{p.quantity:<12}{p.price:<10.2f}")

    def update_stock(self, pid, qty, is_adding=True):
        for p in self.products:
            if p.id == pid:
                if is_adding:
                    p.quantity += qty
                    print(f"\nĐã nhập thêm {qty} sản phẩm.")
                else:
                    if p.quantity >= qty:
                        p.quantity -= qty
                        print(f"\nĐã xuất {qty} sản phẩm.")
                    else:
                        print("\nKhông đủ hàng trong kho!")
                return
        print("\nKhông tìm thấy sản phẩm!")

    def search_product(self, pid):
        for p in self.products:
            if p.id == pid:
                print("\nThông tin sản phẩm:")
                print(f"ID: {p.id} | Tên: {p.name} | Số lượng: {p.quantity} | Giá: {p.price:.2f}")
                return
        print("\nKhông tìm thấy sản phẩm!")

    def delete_product(self, pid):
        for i, p in enumerate(self.products):
            if p.id == pid:
                del self.products[i]
                print("\nSản phẩm đã bị xóa!")
                return
        print("\nKhông tìm thấy sản phẩm để xóa!")

def main():
    warehouse = Warehouse()

    while True:
        print("\n========== QUẢN LÝ KHO ==========")
        print("1. Thêm sản phẩm")
        print("2. Hiển thị danh sách sản phẩm")
        print("3. Nhập kho")
        print("4. Xuất kho")
        print("5. Tìm kiếm sản phẩm")
        print("6. Xóa sản phẩm")
        print("0. Thoát")
        choice = input("Chọn: ")

        if choice == '1':
            try:
                pid = int(input("\nNhập ID sản phẩm: "))
                name = input("Nhập tên sản phẩm: ")
                quantity = int(input("Nhập số lượng: "))
                price = float(input("Nhập giá: "))
                warehouse.add_product(pid, name, quantity, price)
            except ValueError:
                print("Dữ liệu không hợp lệ. Vui lòng thử lại.")
        elif choice == '2':
            warehouse.display_products()
        elif choice == '3':
            try:
                pid = int(input("\nNhập ID sản phẩm: "))
                quantity = int(input("Nhập số lượng cần nhập: "))
                warehouse.update_stock(pid, quantity, True)
            except ValueError:
                print("Dữ liệu không hợp lệ.")
        elif choice == '4':
            try:
                pid = int(input("\nNhập ID sản phẩm: "))
                quantity = int(input("Nhập số lượng cần xuất: "))
                warehouse.update_stock(pid, quantity, False)
            except ValueError:
                print("Dữ liệu không hợp lệ.")
        elif choice == '5':
            try:
                pid = int(input("\nNhập ID sản phẩm: "))
                warehouse.search_product(pid)
            except ValueError:
                print("Dữ liệu không hợp lệ.")
        elif choice == '6':
            try:
                pid = int(input("\nNhập ID sản phẩm cần xóa: "))
                warehouse.delete_product(pid)
            except ValueError:
                print("Dữ liệu không hợp lệ.")
        elif choice == '0':
            warehouse.save_data()
            print("\nDữ liệu đã được lưu. Thoát chương trình...")
            break
        else:
            print("\nLựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
