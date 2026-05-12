import customtkinter as ctk
from view.quan_ly_luong_view import AppQuanLyLuong

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")
    
    root = ctk.CTk()
    app = AppQuanLyLuong(root)
    root.mainloop()