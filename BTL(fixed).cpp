#include <bits/stdc++.h>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
const long long MOD = 1e9 + 7; 

using namespace std;



class SanPham {
private:
    int id;
    string ten;
    string hang;
    double gia;
    int nhap;
    int tonkho;

public:
    // khoi tao gia tri
    SanPham(int id, const string& ten, const string& hang, double gia, const int nhap, int tonkho)
        : id(id), ten(ten), hang(hang), gia(gia), nhap(nhap), tonkho(tonkho) {}

    // Getter và Setter
    int getId() const { return id; }
    string getTen() const { return ten; }
    string getHang() const { return hang; }
    double getGia() const { return gia; }
    int getnhap() const {return nhap;}
    int gettonkho() const {return tonkho;}

    void setGia(double giaMoi) { gia = giaMoi; }
	void settonkho(double soluong) { tonkho = tonkho - soluong; } 
    // hien thi san pham
    void hienThi() const {
        cout << id << ". " << ten << " - " << hang << " - " << gia <<  " VND" << endl;
    }

    
};

class KhachHang {
private:
    int id;
    string ten;
    int LanMua;

public:
    // khoi tao gia tri
    KhachHang(int id,const string& ten, int LanMua)
        : id(id), ten(ten), LanMua(LanMua) {}

    // Getter và Setter
    int getId() const { return id; }
    string getTen() const { return ten; }
    int getLanMua() const { return LanMua; }

    void tangLanMua() { LanMua++; }
    void setLanMua(int lanMuaMoi) { LanMua = lanMuaMoi; }
	void setten(string tenMoi) { ten = tenMoi;}
    // hien thi khach hang
    void hienThi() const {
        cout << id << ". " << ten << " - So lan mua: " << LanMua << endl;
    }
};

string formatNumber(long long num) {
    string s = to_string(num);
    int insertPosition = s.length() - 3;
    while (insertPosition > 0) {
        s.insert(insertPosition, ",");
        insertPosition -= 3;
    }
    return s;
}

vector<SanPham> docSanPhamTuFile(const string &tenTep) {
    vector<SanPham> danhSachSanPham;
    ifstream file(tenTep.c_str());
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
        int nhap,tonkho;
        double gia;

        // doc thong tin san pham
        if (getline(iss, tam, ',')) id = stoi(tam);
        if (getline(iss, tam, ',')) ten = tam;
        if (getline(iss, tam, ',')) hang = tam;
        if (getline(iss, tam, ',')) gia = stod(tam);
		if (getline(iss, tam, ',')) nhap = stoi(tam);
		if (getline(iss, tam, ',')) tonkho = stoi(tam);
        // them san pham vao danh sach
        danhSachSanPham.push_back(SanPham(id, ten, hang, gia, nhap, tonkho));
    }

    return danhSachSanPham;
}
vector<KhachHang> docDanhSachKhachHang(const string &tenTep) {
    vector<KhachHang> danhSachKhachHang;
    ifstream file(tenTep.c_str());
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
    ofstream file(tenTep.c_str());
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

void luuSanPham(const string &tenTep, const vector<SanPham> &danhSachSanPham) {
    ofstream file(tenTep.c_str());
    if (!file.is_open()) {
        cerr << "Khong the mo file de ghi!" << endl;
        return;
    }

    for (size_t i=0;i< danhSachSanPham.size();i++) {
        file << danhSachSanPham[i].getId() << "," 
			 << danhSachSanPham[i].getTen() << "," 
			 << danhSachSanPham[i].getHang() << ","
			 << danhSachSanPham[i].getGia() << ","
			 << danhSachSanPham[i].getnhap() << ","
			 << danhSachSanPham[i].gettonkho() << endl;
    }
    file.close();
}


long long tinhTongTien(vector<SanPham> &danhSachSanPham,const  vector<int> &idDaChon, KhachHang &khachhang) {
    long long tongTien = 0;
    cout << endl << endl << endl;
    cout << "------------------------------------" << endl;
    
    for (size_t i = 0; i < idDaChon.size(); i=i+2) {
    	long long giaSanPham = static_cast<long long>(danhSachSanPham[idDaChon[i] - 1].getGia()) * idDaChon[i + 1];
        tongTien += giaSanPham % MOD;
		tongTien %= MOD; // Su dung dong du
        cout << danhSachSanPham[idDaChon[i]-1].getTen() << " " 
			 << danhSachSanPham[idDaChon[i]-1].getGia() << " " 
			 << idDaChon[i+1] << " " 
			 << formatNumber(static_cast<long long>(danhSachSanPham[idDaChon[i]-1].getGia()*idDaChon[i+1]))  << endl;
		danhSachSanPham[idDaChon[i]-1].settonkho(idDaChon[i+1]);
		luuSanPham("sanpham.txt", danhSachSanPham);
    }
    
    if(khachhang.getLanMua() % 1000 == 0 && khachhang.getLanMua() != 0){
    	cout << "Chuc mung! Khach hang " << khachhang.getTen()
             << " da dat moc " << khachhang.getLanMua() << " lan mua hang."
             << " Quy khach duoc giam gia 70% cho lan mua nay." << endl
             << " Tong tien(chua ap dung uu dai): " << formatNumber(static_cast<long long>(tongTien)) << endl
             << " Giam gia: -" << formatNumber(static_cast<long long>(tongTien*0.7)) << endl; 
             
        tongTien = tongTien*0.3;
	}
    
    return tongTien;
}

void thanhToan( vector<SanPham> &danhSachSanPham, vector<KhachHang> &danhSachKhachHang) {
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
        cout << "Nhap so luong: ";
        cin >> id; 
		while( id == 0 ) { 
			cout << "So luong phai khac 0. Hay nhap lai so luong: ";
			cin >> id;
		}
		
        idDaChon.push_back(id);
        cout << "Nhap ID san pham da mua (0 de ket thuc): ";
    }

    // Tinh tong tien
    double tongTien = tinhTongTien(danhSachSanPham, idDaChon, *khachHang);
    cout << "--------------------" << endl;
    cout << "Tong tien: " << formatNumber(static_cast<long long>(tongTien)) << " VND" << endl;

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
        cout << "3. Sua so lan mua cua khach hang" << endl;
        cout << "4. Sua ten cua khach hang" << endl;
        cout << "5. Xoa khach hang" << endl;
        cout << "6. Tim kiem khach hang" << endl;
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
            // Sua thong tin khach hang
            string ten;
            cout << "Nhap ten khach hang can sua: ";
            cin.ignore();
            getline(cin, ten);
            bool found = false;

            for (size_t i = 0; i < danhSachKhachHang.size(); ++i) {
                if (danhSachKhachHang[i].getTen() == ten) {
                    string tenMoi;
                    cout << "Nhap ten moi: ";
                    getline(cin,tenMoi);
                    danhSachKhachHang[i].setten(tenMoi);
                    found = true;
                    cout << "Da sua ten khach hang thanh: " << tenMoi << endl;
                    break;
                }
            }

            if (!found) {
                cout << "Khong tim thay khach hang: " << ten << endl;
            }

            // Luu danh sách khách hàng vào file
            luuKhachHang("khach_quen.txt", danhSachKhachHang);

        } else if (chon == 5) {
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
                danhSachKhachHang[i] = KhachHang(i + 1, danhSachKhachHang[i].getTen(), danhSachKhachHang[i].getLanMua() );
            }

            // Luu danh sach khach hang vào file
            luuKhachHang("khach_quen.txt", danhSachKhachHang);

        } else if (chon == 6) {
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
        cout << "0. Ket thuc chuong trinh" << endl;
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

