import tkinter.messagebox as messagebox
import pandas as pd
import customtkinter as ctk

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

        tong_gio_lam_them = self.df["Giờ làm thêm"].sum()
        tong_lcb = self.df["Lương cơ bản"].sum()

        if tong_lcb > 0:
            ty_le_tang_truong = ((tong_quy_luong - tong_lcb) / tong_lcb) * 100
        else:
            ty_le_tang_truong = 0

        noi_dung = (
            "BÁO CÁO THỐNG KÊ\n"
            "--------------------------\n"
            "- Công thức Lương thực nhận:\n"
            "  Lương cơ bản + Thưởng - Phạt + (Giờ làm thêm * 100,000 VNĐ)\n\n"
            f"- Thống kê tổng số giờ làm thêm: {tong_gio_lam_them:,.0f} giờ\n"
            f"- Tỷ lệ tăng trưởng lương trung bình: {ty_le_tang_truong:,.2f}%\n"
        )
        messagebox.showinfo("Thống kê chi tiết", noi_dung)

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

    def mo_cua_so_nhap_lieu(self, is_edit=False, data=None):
        window = ctk.CTkToplevel(self.view.root)
        window.geometry("450x700")
        window.transient(self.view.root)
        window.grab_set()

        if not is_edit:
            window.title("Thêm nhân viên mới")
        else:
            window.title("Sửa thông tin nhân viên")

        khung_nhap = ctk.CTkFrame(window)
        khung_nhap.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(khung_nhap, text="Mã Nhân Viên:", font=("Arial", 13, "bold")).pack(anchor="w", padx=20, pady=(10, 0))
        o_ma_nv = ctk.CTkEntry(khung_nhap, width=380, placeholder_text="Nhập mã nhân viên...")
        o_ma_nv.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(khung_nhap, text="Họ và Tên:", font=("Arial", 13, "bold")).pack(anchor="w", padx=20, pady=(5, 0))
        o_ten = ctk.CTkEntry(khung_nhap, width=380, placeholder_text="Nhập họ và tên...")
        o_ten.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(khung_nhap, text="Chức vụ:", font=("Arial", 13, "bold")).pack(anchor="w", padx=20, pady=(5, 0))
        o_chuc_vu = ctk.CTkEntry(khung_nhap, width=380, placeholder_text="Nhập chức vụ...")
        o_chuc_vu.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(khung_nhap, text="Lương cơ bản (VNĐ):", font=("Arial", 13, "bold")).pack(anchor="w", padx=20, pady=(5, 0))
        o_luong_cb = ctk.CTkEntry(khung_nhap, width=380, placeholder_text="Ví dụ: 5000000")
        o_luong_cb.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(khung_nhap, text="Tiền thưởng (VNĐ):", font=("Arial", 13, "bold")).pack(anchor="w", padx=20, pady=(5, 0))
        o_thuong = ctk.CTkEntry(khung_nhap, width=380)
        o_thuong.insert(0, "0")
        o_thuong.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(khung_nhap, text="Tiền phạt (VNĐ):", font=("Arial", 13, "bold")).pack(anchor="w", padx=20, pady=(5, 0))
        o_phat = ctk.CTkEntry(khung_nhap, width=380)
        o_phat.insert(0, "0")
        o_phat.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(khung_nhap, text="Giờ làm thêm (100k/giờ):", font=("Arial", 13, "bold")).pack(anchor="w", padx=20, pady=(5, 0))
        o_gio_lam_them = ctk.CTkEntry(khung_nhap, width=380)
        o_gio_lam_them.insert(0, "0")
        o_gio_lam_them.pack(padx=20, pady=(0, 10))

        ctk.CTkLabel(khung_nhap, text="Tổng Lương Thực Nhận (VNĐ):", font=("Arial", 13, "bold"), text_color="#4ade80").pack(anchor="w", padx=20, pady=(5, 0))
        o_tong = ctk.CTkEntry(khung_nhap, width=380, text_color="#4ade80", font=("Arial", 14, "bold"))
        o_tong.insert(0, "0")
        o_tong.configure(state="readonly")
        o_tong.pack(padx=20, pady=(0, 15))

        def tu_dong_tinh_tong(event=None):
            try:
                lcb = float(o_luong_cb.get().strip() or "0")
                thuong = float(o_thuong.get().strip() or "0")
                phat = float(o_phat.get().strip() or "0")
                glt = float(o_gio_lam_them.get().strip() or "0")
                tong = lcb + thuong - phat + (glt * 100000)

                o_tong.configure(state="normal")
                o_tong.delete(0, "end")
                o_tong.insert(0, f"{tong:,.0f}")
                o_tong.configure(state="readonly")
            except ValueError:
                o_tong.configure(state="normal")
                o_tong.delete(0, "end")
                o_tong.insert(0, "Lỗi số liệu")
                o_tong.configure(state="readonly")

        o_luong_cb.bind("<KeyRelease>", tu_dong_tinh_tong)
        o_thuong.bind("<KeyRelease>", tu_dong_tinh_tong)
        o_phat.bind("<KeyRelease>", tu_dong_tinh_tong)
        o_gio_lam_them.bind("<KeyRelease>", tu_dong_tinh_tong)

        if is_edit and data:
            o_ma_nv.insert(0, str(data.get("Mã NV", "")))
            o_ma_nv.configure(state="disabled")
            o_ten.insert(0, str(data.get("Họ Tên", "")))
            o_chuc_vu.insert(0, str(data.get("Chức vụ", "")))

            o_luong_cb.insert(0, str(data.get("Lương cơ bản", "0")).replace(',', ''))
            o_thuong.delete(0, "end")
            o_thuong.insert(0, str(data.get("Thưởng", "0")).replace(',', ''))
            o_phat.delete(0, "end")
            o_phat.insert(0, str(data.get("Phạt", "0")).replace(',', ''))
            o_gio_lam_them.delete(0, "end")
            o_gio_lam_them.insert(0, str(data.get("Giờ làm thêm", "0")).replace(',', ''))

            tu_dong_tinh_tong()

        def luu_thong_tin():
            try:
                ma_nv = o_ma_nv.get().strip()
                ho_ten = o_ten.get().strip()
                chuc_vu = o_chuc_vu.get().strip()
                luong_cb_text = o_luong_cb.get().strip()

                if ma_nv == "" or ho_ten == "" or chuc_vu == "" or luong_cb_text == "":
                    messagebox.showwarning("Cảnh báo", "Bạn chưa nhập đủ thông tin bắt buộc!", parent=window)
                    return

                luong_cb = float(luong_cb_text or "0")
                thuong = float(o_thuong.get().strip() or "0")
                phat = float(o_phat.get().strip() or "0")
                gio_lam = float(o_gio_lam_them.get().strip() or "0")

                luong_thuc_nhan = luong_cb + thuong - phat + (gio_lam * 100000)

                new_data = {
                    "Mã NV": ma_nv,
                    "Họ Tên": ho_ten,
                    "Chức vụ": chuc_vu,
                    "Lương cơ bản": luong_cb,
                    "Thưởng": thuong,
                    "Phạt": phat,
                    "Giờ làm thêm": gio_lam,
                    "Lương thực nhận": luong_thuc_nhan
                }

                if is_edit:
                    self.model.update_employee(ma_nv, new_data)
                else:
                    if not self.df.empty and ma_nv in self.df["Mã NV"].values:
                        messagebox.showwarning("Lỗi", "Mã nhân viên đã tồn tại!", parent=window)
                        return
                    self.model.add_employee(new_data)

                self.lam_moi_bang()
                window.destroy()
                messagebox.showinfo("Thành công", "Đã lưu thông tin thành công.")
            except ValueError:
                messagebox.showwarning("Lỗi", "Vui lòng nhập số hợp lệ cho lương, thưởng, phạt, giờ làm!", parent=window)

        ctk.CTkButton(khung_nhap, text="LƯU THÔNG TIN", font=("Arial", 14, "bold"), command=luu_thong_tin, height=40).pack(pady=10)

    def mo_cua_so_them(self):
        self.mo_cua_so_nhap_lieu(is_edit=False)

    def mo_cua_so_sua(self):
        selected = None
        for item in self.view.bang.get_children():
            values = self.view.bang.item(item, "values")
            if values[0] == "☑":
                if selected is not None:
                    messagebox.showwarning("Cảnh báo", "Vui lòng chỉ chọn 1 nhân viên để sửa.")
                    return
                selected = values

        if not selected:
            selections = self.view.bang.selection()
            if len(selections) == 1:
                selected = self.view.bang.item(selections[0], "values")
            elif len(selections) > 1:
                messagebox.showwarning("Cảnh báo", "Vui lòng chỉ chọn 1 nhân viên để sửa.")
                return
            else:
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn 1 nhân viên để sửa.")
                return

        ma_nv = selected[1]
        row_data = self.df[self.df["Mã NV"] == str(ma_nv)]
        if not row_data.empty:
            data_dict = row_data.iloc[0].to_dict()
            self.mo_cua_so_nhap_lieu(is_edit=True, data=data_dict)

    def xoa_nhan_vien(self):
        items_to_delete = []
        for item in self.view.bang.get_children():
            values = self.view.bang.item(item, "values")
            if values[0] == "☑":
                items_to_delete.append(str(values[1]))

        if not items_to_delete:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một nhân viên để xóa.")
            return

        if messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa {len(items_to_delete)} nhân viên đã chọn?"):
            self.model.delete_employee(items_to_delete)
            self.lam_moi_bang()
            messagebox.showinfo("Thành công", "Đã xóa thành công.")

    def click_chon_checkbox(self, event):
        region = self.view.bang.identify("region", event.x, event.y)
        if region == "cell":
            column = self.view.bang.identify_column(event.x)
            if column == '#1':
                item = self.view.bang.identify_row(event.y)
                values = list(self.view.bang.item(item, "values"))
                if values[0] == "☐":
                    values[0] = "☑"
                else:
                    values[0] = "☐"
                self.view.bang.item(item, values=values)

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
