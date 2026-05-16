# Phần mềm Quản lý Lương Nhân viên

Đây là một ứng dụng quản lý lương nhân viên được xây dựng bằng ngôn ngữ Python, sử dụng thư viện **CustomTkinter** cho giao diện hiện đại và **Pandas** để xử lý dữ liệu.

## 📁 Cấu trúc dự án (Mô hình MVC)

Dự án được tổ chức theo mô hình **Model-View-Controller (MVC)** để dễ dàng quản lý và bảo trì:

*   **`main.py`**: Điểm khởi đầu của ứng dụng. Dùng để cấu hình giao diện và chạy vòng lặp chính.
*   **`view/`**: Chứa toàn bộ mã nguồn liên quan đến giao diện người dùng (UI).
    *   `quan_ly_luong_view.py`: Định nghĩa các thành phần như bảng dữ liệu, nút bấm, và thanh trạng thái.
*   **`model/`**: Chứa logic xử lý dữ liệu.
    *   `quan_ly_luong_model.py`: Chịu trách nhiệm đọc/ghi dữ liệu từ file CSV (`nhanvien.csv`).
*   **`controller/`**: Chứa logic điều khiển.
    *   `quan_ly_luong_controller.py`: Kết nối giữa Giao diện và Dữ liệu, xử lý các sự kiện khi người dùng tương tác (bấm nút, tìm kiếm, sắp xếp).

## ✨ Chức năng chính

1.  **Quản lý Nhân Viên (CRUD)**: 
    *   **Thêm nhân viên mới**: Giao diện nhập liệu trực quan, xếp dọc từng dòng rõ ràng, tự động tính toán tổng lương thực nhận ngay khi đang gõ.
    *   **Sửa thông tin**: Hỗ trợ điền sẵn dữ liệu cũ, thay đổi nhanh chóng.
    *   **Xóa nhân viên**: Chọn bằng thao tác đánh dấu tick (☑) tiện lợi trên bảng.
2.  **Hiển thị danh sách**: Xem thông tin nhân viên (Mã NV, Họ tên, Chức vụ, Lương...) dưới dạng bảng chuyên nghiệp.
3.  **Tìm kiếm**: Tìm kiếm nhanh nhân viên theo Mã hoặc Họ tên.
4.  **Sắp xếp**: Hỗ trợ sắp xếp theo Mã nhân viên, Tên (A-Z), hoặc Lương (Cao/Thấp).
5.  **Thống kê chi tiết**: Tính toán nhanh Sĩ số, Lương trung bình, Tổng quỹ lương, cùng với cửa sổ Báo cáo chi tiết (Tổng số giờ làm thêm, Tỷ lệ tăng trưởng lương).
6.  **Giao diện hiện đại**: Sử dụng Dark Mode giúp giảm mỏi mắt và trông chuyên nghiệp hơn.
7.  **Quản lý dữ liệu**: Hỗ trợ Nhập/Xuất file CSV (Đang phát triển thêm).

## 🛠 Yêu cầu hệ thống

Để chạy ứng dụng, bạn cần cài đặt các thư viện sau:

```bash
pip install customtkinter pandas
```

## 🚀 Cách chạy chương trình

Chạy lệnh sau từ thư mục gốc của dự án:

```bash
python main.py
```
