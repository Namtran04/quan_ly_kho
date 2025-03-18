#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

class SanPham {
private:
    int id;
    string ten;
    string hang;
    double gia;

public:
    // khoi tao gia tri
    SanPham(int id, const string& ten, const string& hang, double gia)
        : id(id), ten(ten), hang(hang), gia(gia) {}

    // Getter và Setter
    int getId() const { return id; }
    string getTen() const { return ten; }
    string getHang() const { return hang; }
    double getGia() const { return gia; }

    void setGia(double giaMoi) { gia = giaMoi; }

    // hien thi san pham
    void hienThi() const {
        cout << id << ". " << ten << " - " << hang << " - " << gia << " VND" << endl;
    }

    
};

class KhachHang {
private:
    int id;
    string ten;
    int LanMua;

public:
    // khoi tao gia tri
    KhachHang(int id, const string& ten, int LanMua)
        : id(id), ten(ten), LanMua(LanMua) {}

    // Getter và Setter
    int getId() const { return id; }
    string getTen() const { return ten; }
    int getLanMua() const { return LanMua; }

    void tangLanMua() { LanMua++; }
    void setLanMua(int lanMuaMoi) { LanMua = lanMuaMoi; }

    // hien thi khach hang
    void hienThi() const {
        cout << id << ". " << ten << " - So lan mua: " << LanMua << endl;
    }
};
vector<SanPham> docSanPhamTuFile(const string &tenTep) {
    vector<SanPham> danhSachSanPham;
    ifstream file(tenTep);
    if (!file) {
        cerr << "Loi khi mo file: " << tenTep << endl;
        return danhSachSanPham;
    }

    string dong;
    while (getline(file, dong)) {
        istringstream iss(dong);
        string tam;
        int id;
        string ten, hang;
        double gia;

        // doc thong tin san pham
        if (getline(iss, tam, ',')) id = stoi(tam);
        if (getline(iss, tam, ',')) ten = tam;
        if (getline(iss, tam, ',')) hang = tam;
        if (getline(iss, tam, ',')) gia = stod(tam);

        // them san pham vao danh sach
        danhSachSanPham.push_back(SanPham(id, ten, hang, gia));
    }

    return danhSachSanPham;
}
vector<KhachHang> docDanhSachKhachHang(const string &tenTep) {
    vector<KhachHang> danhSachKhachHang;
    ifstream file(tenTep);
    if (!file.is_open()) {
        cerr << "Khong the mo file khach hang" << endl;
        return danhSachKhachHang;
    }

    string dong;
    while (getline(file, dong)) {
        istringstream iss(dong);
        string tam;
        int id;
        string ten;
        int LanMua;

        if (getline(iss, tam, ',')) id = stoi(tam);
        if (getline(iss, tam, ',')) ten = tam;
        if (getline(iss, tam, ',')) LanMua = stoi(tam);

        danhSachKhachHang.push_back(KhachHang(id, ten, LanMua));
    }

    return danhSachKhachHang;
}
void luuKhachHang(const string &tenTep, const vector<KhachHang> &danhSachKhachHang) {
    ofstream file(tenTep);
    if (!file.is_open()) {
        cerr << "Khong the mo file de ghi!" << endl;
        return;
    }

    for (size_t i=0;i< danhSachKhachHang.size();i++) {
        file << danhSachKhachHang[i].getId() << "," << danhSachKhachHang[i].getTen() << "," << danhSachKhachHang[i].getLanMua() << endl;
    }
    file.close();
}
void hienThiSanPham(const vector<SanPham> &danhSachSanPham) {
    for (size_t i=0;i< danhSachSanPham.size();i++) {
        danhSachSanPham[i].hienThi();
    }
}
void hienThiKhachHang(const vector<KhachHang> &danhSachKhachHang) {
    for ( size_t i=0;i< danhSachKhachHang.size();i++) {
        danhSachKhachHang[i].hienThi();
    }
}

double tinhTongTien(const vector<SanPham> &danhSachSanPham,const  vector<int> &idDaChon, KhachHang &khachhang) {
    double tongTien = 0;
    cout << endl << endl << endl;
    cout << "------------------------------------" << endl;
    for (size_t i = 0; i < idDaChon.size(); ++i) {
        tongTien = tongTien+ danhSachSanPham[idDaChon[i]-1].getGia();
        cout << danhSachSanPham[idDaChon[i]-1].getTen() << " " << danhSachSanPham[idDaChon[i]-1].getGia() << endl;
    }
    if(khachhang.getLanMua()>20){
    	cout << "So lan mua cua quy khach la: " << khachhang.getLanMua() << ". Do lon hon 20 nen quy khach duoc giam 10\%" << endl;
        tongTien = tongTien*0.9;
	}
    
    return tongTien;
}

void thanhToan(const vector<SanPham> &danhSachSanPham, vector<KhachHang> &danhSachKhachHang) {
    string tenKhachHang;
    cout << "Nhap ten khach hang: ";
    cin.ignore();
    getline(cin, tenKhachHang);

    // Tim khach hang
    KhachHang* khachHang = NULL;
    for (size_t i=0;i< danhSachKhachHang.size();i++) {
        if (danhSachKhachHang[i].getTen() == tenKhachHang) {
            khachHang = &danhSachKhachHang[i];
            break;
        }
    }

    if (!khachHang) {
        // Neu khach hang chua mua bao gio, them moi
        cout << "Them khach hang moi vao danh sach." << endl;
        danhSachKhachHang.push_back(KhachHang(danhSachKhachHang.size() + 1, tenKhachHang, 0));
        khachHang = &danhSachKhachHang.back();
    }

    // hien thi danh sach san pham
    hienThiSanPham(danhSachSanPham);

    // Nhap san pham mua
    vector<int> idDaChon;
    int id;
    cout << "Nhap ID san pham da mua (0 de ket thuc): ";
    while (cin >> id && id != 0) {
        idDaChon.push_back(id);
        cout << "Nhap ID san pham da mua (0 de ket thuc): ";
    }

    // Tinh tong tien
    double tongTien = tinhTongTien(danhSachSanPham, idDaChon, *khachHang);
    cout << "Tong tien: " << tongTien << " VND" << endl;

    // Tang so lan mua cua khach
    khachHang->tangLanMua();

    // Luu danh sach khach hang
    luuKhachHang("khach_quen.txt", danhSachKhachHang);
}

// Ham quan ly khach quen: them, sua, xoa, tim kiem
void quanLyKhachHang(vector<KhachHang> &danhSachKhachHang) {
    int chon;
    do {
        cout << "-----------------------------------------" << endl;
        cout << "1. Hien thi danh sach khach quen" << endl;
        cout << "2. Them khach hang moi" << endl;
        cout << "3. Sua thong tin khach hang" << endl;
        cout << "4. Xoa khach hang" << endl;
        cout << "5. Tim kiem khach hang" << endl;
        cout << "0. Quay lai menu chinh" << endl;
        cout << "Nhap lua chon: ";
        cin >> chon;

        if (chon == 1) {
            // hien thi danh sach khach hang
            hienThiKhachHang(danhSachKhachHang);

        } else if (chon == 2) {
            // Them khach hang moi
            string ten;
            cout << "Nhap ten khach hang moi: ";
            cin.ignore();
            getline(cin, ten);
            KhachHang khachhangmoi(danhSachKhachHang.size() + 1, ten, 0);
            danhSachKhachHang.push_back(khachhangmoi);
            cout << "Da them khach hang moi: " << ten << endl;

            // Luu danh sách khách hàng vào file
            luuKhachHang("khach_quen.txt", danhSachKhachHang);

        } else if (chon == 3) {
            // Sua thong tin khach hang
            string ten;
            cout << "Nhap ten khach hang can sua: ";
            cin.ignore();
            getline(cin, ten);
            bool found = false;

            for (size_t i = 0; i < danhSachKhachHang.size(); ++i) {
                if (danhSachKhachHang[i].getTen() == ten) {
                    int soLanMuaMoi;
                    cout << "Nhap so lan mua moi: ";
                    cin >> soLanMuaMoi;
                    danhSachKhachHang[i].setLanMua(soLanMuaMoi);
                    found = true;
                    cout << "Da sua thong tin khach hang: " << ten << endl;
                    break;
                }
            }

            if (!found) {
                cout << "Khong tim thay khach hang: " << ten << endl;
            }

            // Luu danh sách khách hàng vào file
            luuKhachHang("khach_quen.txt", danhSachKhachHang);

        } else if (chon == 4) {
            // Xóa khách hàng
            string ten;
            cout << "Nhap ten khach hang can xoa: ";
            cin.ignore();
            getline(cin, ten);
            bool found = false;

            for (size_t i = 0; i < danhSachKhachHang.size(); ++i) {
                if (danhSachKhachHang[i].getTen() == ten) {
                    danhSachKhachHang.erase(danhSachKhachHang.begin() + i);
                    found = true;
                    cout << "Da xoa khach hang: " << ten << endl;
                    break;
                }
            }

            if (!found) {
                cout << "Khong tim thay khach hang: " << ten << endl;
            }

            // Cap nhat lai so thu tu (id) cho cac khach hang sau khi xoa
            for (size_t i = 0; i < danhSachKhachHang.size(); ++i) {
                danhSachKhachHang[i] = KhachHang(i + 1, danhSachKhachHang[i].getTen(), danhSachKhachHang[i].getLanMua());
            }

            // Luu danh sach khach hang vào file
            luuKhachHang("khach_quen.txt", danhSachKhachHang);

        } else if (chon == 5) {
            // Tim kiem khach hang
            string ten;
            cout << "Nhap ten khach hang can tim: ";
            cin.ignore();
            getline(cin, ten);
            bool found = false;

            for (size_t i = 0; i < danhSachKhachHang.size(); ++i) {
                if (danhSachKhachHang[i].getTen() == ten) {
                    danhSachKhachHang[i].hienThi();  // Hien thi thong tin khach hang
                    found = true;
                    break;
                }
            }

            if (!found) {
                cout << "Khong tim thay khach hang: " << ten << endl;
            }
        }

    } while (chon != 0);
}

int main() {
    vector<SanPham> danhSachSanPham = docSanPhamTuFile("sanpham.txt");
    vector<KhachHang> danhSachKhachHang = docDanhSachKhachHang("khach_quen.txt");

    int chon;
    do {
        cout << "-----------------------------------------" << endl;
        cout << "1. Xem danh sach san pham va mua hang" << endl;
        cout << "2. Quan ly khach quen" << endl;
        cout << "0. Thoat" << endl;
        cout << "Nhap lua chon: ";
        cin >> chon;

        if (chon == 1) {
            thanhToan(danhSachSanPham, danhSachKhachHang);
        } else if (chon == 2) {
            quanLyKhachHang(danhSachKhachHang);
        }
    } while (chon != 0);

    return 0;
}
