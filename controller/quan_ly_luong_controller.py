import tkinter.messagebox as messagebox
import pandas as pd

class QuanLyLuongController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.df = self.model.get_dataframe()

    def nhap_csv(self):
        messagebox.showinfo("Nhập CSV", "Chức năng nhập CSV chưa được triển khai.")

    def xuat_csv(self):
        messagebox.showinfo("Xuất CSV", "Chức năng xuất CSV chưa được triển khai.")

    def hien_thi_thong_tin(self):
        messagebox.showinfo("Giới thiệu", "Phần mềm quản lý lương nhân viên\nPhiên bản 1.0\nPhát triển bởi TT02B_nhom4")

    def hien_thi_thong_ke(self):
        if self.df.empty:
            messagebox.showinfo("Thống kê", "Không có dữ liệu để thống kê.")
            return
        tong_so_nguoi = len(self.df)
        luong_trung_binh = self.df["Lương thực nhận"].mean()
        tong_quy_luong = self.df["Lương thực nhận"].sum()
        self.view.cap_nhat_trang_thai(tong_so_nguoi, luong_trung_binh, tong_quy_luong)

    def lam_moi_bang(self):
        self.df = self.model.get_dataframe()
        self.view.lam_moi_bang(self.df)

    def tim_kiem(self):
        query = self.view.o_tim_kiem.get().strip().lower()
        if not query:
            self.lam_moi_bang()
            return
        mask = self.df.apply(lambda row: query in str(row["Mã NV"]).lower() or query in str(row["Họ Tên"]).lower(), axis=1)
        filtered = self.df[mask]
        self.view.lam_moi_bang(filtered)

    def mo_cua_so_them(self):
        messagebox.showinfo("Thêm nhân viên", "Chức năng thêm nhân viên chưa được triển khai.")

    def mo_cua_so_sua(self):
        messagebox.showinfo("Sửa thông tin", "Chức năng sửa nhân viên chưa được triển khai.")

    def xoa_nhan_vien(self):
        messagebox.showinfo("Xóa nhân viên", "Chức năng xóa nhân viên chưa được triển khai.")

    def click_chon_checkbox(self, event):
        pass

    def sap_xep(self, option):
        if "Mã nhân viên" in option:
            sort_key = "Mã NV"
            ascending = True
        elif "Tên (A-Z)" in option:
            sort_key = "Họ Tên"
            ascending = True
        elif "Lương (Cao -> Thấp)" in option:
            sort_key = "Lương thực nhận"
            ascending = False
        elif "Lương (Thấp -> Cao)" in option:
            sort_key = "Lương thực nhận"
            ascending = True
        else:
            return
        if self.df.empty:
            return
        self.df = self.df.sort_values(by=sort_key, ascending=ascending).reset_index(drop=True)
        self.view.lam_moi_bang(self.df)
