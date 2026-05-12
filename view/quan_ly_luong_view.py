import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from model.quan_ly_luong_model import QuanLyLuongModel
from controller.quan_ly_luong_controller import QuanLyLuongController

FILE_NAME = "nhanvien.csv"

class AppQuanLyLuong:
    def __init__(self, root):
        self.root = root
        self.root.title("Phần mềm quản lý lương nhân viên")
        self.root.geometry("1100x750")

        self.cac_cot = ["Mã NV", "Họ Tên", "Chức vụ", "Lương cơ bản", "Thưởng", "Phạt", "Giờ làm thêm", "Lương thực nhận"]
        self.cac_cot_ui = ["Chọn"] + self.cac_cot
        
        self.model = QuanLyLuongModel(FILE_NAME)
        self.controller = QuanLyLuongController(self, self.model)
        
        self.ve_giao_dien()
        
    def ve_giao_dien(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", rowheight=25)
        style.map("Treeview", background=[("selected", "#1f538d")])
        style.configure("Treeview.Heading", background="#333333", foreground="white", font=("Arial", 10, "bold"))
                  
        ctk.CTkLabel(self.root, text="PHẦM MỀM QUẢN LÝ LƯƠNG", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(20, 10))

        khung_phia_tren = ctk.CTkFrame(self.root, fg_color="transparent")
        khung_phia_tren.pack(pady=10, padx=20, fill="x")

        ctk.CTkButton(khung_phia_tren, text="Nhập CSV", command=self.controller.nhap_csv, width=100, fg_color="#059669").pack(side="left", padx=5)
        ctk.CTkButton(khung_phia_tren, text="Xuất CSV", command=self.controller.xuat_csv, width=100, fg_color="#0284c7").pack(side="left", padx=5)
        ctk.CTkButton(khung_phia_tren, text="Giới thiệu", command=self.controller.hien_thi_thong_tin, width=100).pack(side="left", padx=5)
        ctk.CTkButton(khung_phia_tren, text="Thống kê", command=self.controller.hien_thi_thong_ke, width=100, fg_color="#a855f7").pack(side="left", padx=5)

        ctk.CTkButton(khung_phia_tren, text="Hiện tất cả", command=self.controller.lam_moi_bang).pack(side="right", padx=5)
        ctk.CTkButton(khung_phia_tren, text="Tìm", command=self.controller.tim_kiem).pack(side="right", padx=5)
        self.o_tim_kiem = ctk.CTkEntry(khung_phia_tren, width=200, placeholder_text="Nhập tên hoặc mã...")
        self.o_tim_kiem.pack(side="right", padx=5)

        khung_chuc_nang = ctk.CTkFrame(self.root, fg_color="transparent")
        khung_chuc_nang.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkButton(khung_chuc_nang, text="Thêm nhân viên", command=self.controller.mo_cua_so_them).pack(side="left", padx=5)
        ctk.CTkButton(khung_chuc_nang, text="Sửa thông tin", command=self.controller.mo_cua_so_sua, fg_color="#facc15", text_color="black").pack(side="left", padx=5)
        ctk.CTkButton(khung_chuc_nang, text="Xóa", command=self.controller.xoa_nhan_vien, fg_color="#ef4444").pack(side="left", padx=5)
        
        self.tieu_chi_sap_xep = ctk.CTkOptionMenu(khung_chuc_nang, values=[
            "Sắp xếp: Mã nhân viên", 
            "Sắp xếp: Tên (A-Z)", 
            "Sắp xếp: Lương (Cao -> Thấp)", 
            "Sắp xếp: Lương (Thấp -> Cao)"
        ], command=self.controller.sap_xep)
        self.tieu_chi_sap_xep.pack(side="left", padx=5)

        khung_chua_bang = ctk.CTkFrame(self.root)
        khung_chua_bang.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.bang = ttk.Treeview(khung_chua_bang, columns=self.cac_cot_ui, show="headings")
        
        for cot in self.cac_cot_ui:
            self.bang.heading(cot, text=cot)
            self.bang.column(cot, anchor="center")
            if cot == "Chọn":
                self.bang.column(cot, width=50, stretch=False)
            
        self.bang.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        
        thanh_cuon = ctk.CTkScrollbar(khung_chua_bang, orientation="vertical", command=self.bang.yview)
        thanh_cuon.pack(side="right", fill="y", padx=(0, 10), pady=10)
        self.bang.configure(yscrollcommand=thanh_cuon.set)
        
        self.bang.bind("<Double-1>", lambda e: self.controller.mo_cua_so_sua())
        self.bang.bind("<ButtonRelease-1>", self.controller.click_chon_checkbox)
        
        self.khung_trang_thai = ctk.CTkFrame(self.root, height=30, corner_radius=0)
        self.khung_trang_thai.pack(side="bottom", fill="x")
        
        self.nhan_trang_thai = ctk.CTkLabel(self.khung_trang_thai, text="Đang tải...", font=("Arial", 12, "bold"))
        self.nhan_trang_thai.pack(side="left", padx=20, pady=5)

        self.controller.lam_moi_bang()

    def cap_nhat_trang_thai(self, tong_so_nguoi, luong_trung_binh, tong_quy_luong):
        if tong_so_nguoi == 0:
            self.nhan_trang_thai.configure(text="Sĩ số: 0 | Chưa có dữ liệu")
            return
            
        chuoi_thong_bao = f"Sĩ số: {tong_so_nguoi} | Lương Trung Bình: {luong_trung_binh:,.0f} VNĐ | Tổng quỹ lương: {tong_quy_luong:,.0f} VNĐ"
        self.nhan_trang_thai.configure(text=chuoi_thong_bao)

    def lam_moi_bang(self, df_hien_thi):
        for item in self.bang.get_children():
            self.bang.delete(item)
            
        for index, dong in df_hien_thi.iterrows():
            dong_da_format = [
                "☐",
                dong["Mã NV"], dong["Họ Tên"], dong["Chức vụ"],
                f"{dong['Lương cơ bản']:,.0f}", f"{dong['Thưởng']:,.0f}", 
                f"{dong['Phạt']:,.0f}", f"{dong['Giờ làm thêm']:,.0f}", f"{dong['Lương thực nhận']:,.0f}"
            ]
            self.bang.insert("", "end", values=dong_da_format)
