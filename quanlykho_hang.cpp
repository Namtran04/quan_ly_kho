#include <iostream>
#include <vector>
#include <string>
#include<bits/stdc++.h>
#include <unordered_map>
#include <iomanip>
#include <vector>
#include <utility>
using namespace std;

class Product {
public:
    int id;
    string name;
    int quantity;
    double price;

    Product(int id, string name, int quantity, double price) {
        this->id = id;
        this->name = name;
        this->quantity = quantity;
        this->price = price;
    }
};

class Warehouse {
private:
    vector<Product> products;
public:
    void addProduct(int id, string name, int quantity, double price) {
        products.push_back(Product(id, name, quantity, price));
        cout << "\nSan pham da duoc them vao kho!" << endl;
    }

    void displayProducts() {
        if (products.empty()) {
            cout << "\nKho hang dang trong!" << endl;
            return;
        }
        cout << "\nDanh sach san pham trong kho:" << endl;
        for (const auto &product : products) {
            cout << "ID: " << product.id << " | Ten: " << product.name << " | So luong: " << product.quantity << " | Gia: " << product.price << endl;
        }
    }

    void updateStock(int id, int qty, bool isAdding) {
        for (auto &product : products) {
            if (product.id == id) {
                if (isAdding) {
                    product.quantity += qty;
                    cout << "\nDa nhap them " << qty << " san pham." << endl;
                } else {
                    if (product.quantity >= qty) {
                        product.quantity -= qty;
                        cout << "\nDa xuat " << qty << " san pham." << endl;
                    } else {
                        cout << "\nKhong du hang trong kho!" << endl;
                    }
                }
                return;
            }
        }
        cout << "\nKhong tim thay san pham!" << endl;
    }

    void searchProduct(int id) {
        for (const auto &product : products) {
            if (product.id == id) {
                cout << "\nThong tin san pham:" << endl;
                cout << "ID: " << product.id << " | Ten: " << product.name << " | So luong: " << product.quantity << " | Gia: " << product.price << endl;
                return;
            }
        }
        cout << "\nKhong tim thay san pham!" << endl;
    }

    void deleteProduct(int id) {
        for (size_t i = 0; i < products.size(); i++) {
            if (products[i].id == id) {
                products.erase(products.begin() + i);
                cout << "\nSan pham da bi xoa!" << endl;
                return;
            }
        }
        cout << "\nKhong tim thay san pham de xoa!" << endl;
    }
};

int main() {
    Warehouse warehouse;
    int choice;
    do {
        cout << "\n========== QUAN LY KHO ==========";
        cout << "\n1. Them san pham";
        cout << "\n2. Hien thi danh sach san pham";
        cout << "\n3. Nhap kho";
        cout << "\n4. Xuat kho";
        cout << "\n5. Tim kiem san pham";
        cout << "\n6. Xoa san pham";
        cout << "\n0. Thoat";
        cout << "\nChon: ";
        cin >> choice;

        int id, quantity;
        string name;
        double price;

        switch (choice) {
            case 1:
                cout << "\nNhap ID san pham: "; cin >> id;
                cout << "Nhap ten san pham: "; cin.ignore(); getline(cin, name);
                cout << "Nhap so luong: "; cin >> quantity;
                cout << "Nhap gia: "; cin >> price;
                warehouse.addProduct(id, name, quantity, price);
                break;
            case 2:
                warehouse.displayProducts();
                break;
            case 3:
                cout << "\nNhap ID san pham: "; cin >> id;
                cout << "Nhap so luong can nhap: "; cin >> quantity;
                warehouse.updateStock(id, quantity, true);
                break;
            case 4:
                cout << "\nNhap ID san pham: "; cin >> id;
                cout << "Nhap so luong can xuat: "; cin >> quantity;
                warehouse.updateStock(id, quantity, false);
                break;
            case 5:
                cout << "\nNhap ID san pham: "; cin >> id;
                warehouse.searchProduct(id);
                break;
            case 6:
                cout << "\nNhap ID san pham can xoa: "; cin >> id;
                warehouse.deleteProduct(id);
                break;
            case 0:
                cout << "\nThoat chuong trinh...";
                break;
            default:
                cout << "\nLua chon khong hop le!";
        }
    } while (choice != 0);

    return 0;
}
