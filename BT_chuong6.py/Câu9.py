import tkinter as tk
from tkinter import ttk, messagebox

# --- Các hàm chức năng ---

def ham_doi_mat_khau():
    """Hàm này được gọi khi nhấn nút OK"""
    old_pass = entry_old.get()
    new_pass = entry_new.get()
    confirm_pass = entry_confirm.get()

    if not old_pass or not new_pass or not confirm_pass:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return

    if new_pass == confirm_pass:
        print(f"Đổi mật khẩu cho: {old_pass} -> {new_pass}")
        messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")
    else:
        messagebox.showerror("Lỗi", "Mật khẩu mới và xác nhận không khớp!")

def ham_thoat():
    """Hàm này được gọi khi nhấn nút Cancel"""
    root.destroy()

# --- Bước 1: Tạo cửa sổ chính ---
root = tk.Tk()
root.title("Enter New Password")
root.geometry("380x180") # Kích thước nhỏ lại vì không có header
root.eval('tk::PlaceWindow . center')
root.resizable(width=True, height=False) 

# --- Bước 2: Tạo MỘT Frame chính duy nhất ---
# Thêm padding (khoảng đệm) trực tiếp vào Frame
main_frame = ttk.Frame(root, padding="15 15 15 15")
# Dùng .pack() để Frame lấp đầy cửa sổ
main_frame.pack(expand=True, fill='both') 

# --- Bước 3: Đặt TẤT CẢ widget vào main_frame bằng .grid() ---



# Dòng 1: Old Password
label_old = ttk.Label(main_frame, text="Old Password") 
# Căn lề phải (sticky="e") cho thẳng hàng
label_old.grid(row=1, column=0, sticky="e", padx=5, pady=5) 

entry_old = ttk.Entry(main_frame, show="*") 
entry_old.grid(row=1, column=1, padx=5, pady=5, sticky="ew") # Lấp đầy ngang

# Dòng 2: New Password
label_new = ttk.Label(main_frame, text="New Password") 
label_new.grid(row=2, column=0, sticky="e", padx=5, pady=5) # Căn lề phải

entry_new = ttk.Entry(main_frame, show="*") 
entry_new.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Dòng 3: Enter New Password Again (Xác nhận)
label_confirm = ttk.Label(main_frame, text="Enter New Password Again") 
label_confirm.grid(row=3, column=0, sticky="e", padx=5, pady=5) # Căn lề phải

entry_confirm = ttk.Entry(main_frame, show="*") 
entry_confirm.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

# Dòng 4: Các nút bấm
button_ok = ttk.Button(main_frame, text="OK", command=ham_doi_mat_khau) 
button_ok.grid(row=4, column=0, sticky="e", padx=10, pady=10) # Căn phải ở cột 0

button_cancel = ttk.Button(main_frame, text="Cancel", command=ham_thoat) 
button_cancel.grid(row=4, column=1, sticky="w", padx=10, pady=10) # Căn trái ở cột 1

# --- Bước 4: Cấu hình co giãn cho grid ---
# Chỉ cho phép cột 1 (chứa ô Entry) co giãn
main_frame.columnconfigure(1, weight=1) 

# --- Bước 5: Chạy ứng dụng ---
root.mainloop()