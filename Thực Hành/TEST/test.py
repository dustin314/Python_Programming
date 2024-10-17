# ỨNG DỤNG ĐẶT LỊCH HẸN
from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime
import psycopg2

# Kết nối đến cơ sở dữ liệu
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="dbtest",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể kết nối đến cơ sở dữ liệu!\n{e}")
        return None

# Kết nối đến cơ sở dữ liệu
conn = connect_to_db()
c = conn.cursor()

# Tạo bảng 
# c.execute('''CREATE TABLE IF NOT EXISTS appointments (
#                 id SERIAL PRIMARY KEY,
#                 name VARCHAR(100),
#                 phone VARCHAR(15),
#                 appointment_date TIMESTAMP,
#                 service VARCHAR(100))''')
# conn.commit()

# Lớp Tooltip
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tip_window = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("Arial", 10, "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

# Hàm thêm lịch hẹn
def add_appointment():
    if name_entry.get() == "" or phone_entry.get() == "" or service_entry.get() == "":
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
    else:
        try:
            appointment_date = datetime.strptime(date_entry.get(), "%Y-%m-%d")
            c.execute("INSERT INTO appointments (name, phone, appointment_date, service) VALUES (%s, %s, %s, %s)", 
                      (name_entry.get(), phone_entry.get(), appointment_date, service_entry.get()))
            conn.commit()
            messagebox.showinfo("Thành công", "Đã thêm lịch hẹn!")
            clear_entries()
            show_appointments()
        except ValueError:
            messagebox.showerror("Lỗi", "Ngày không đúng định dạng!")
        except Exception as e:
            conn.rollback()
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# Hàm hiển thị tất cả lịch hẹn
def show_appointments():
    for row in tree.get_children():
        tree.delete(row)
    c.execute("SELECT * FROM appointments")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", "end", values=(row[0], row[1], row[2], row[3].strftime("%Y-%m-%d"), row[4]))

# Hàm xóa một lịch hẹn
def delete_appointment():
    try:
        selected_item = tree.selection()[0]
        appointment_id = tree.item(selected_item)["values"][0]
        c.execute("DELETE FROM appointments WHERE id=%s", (appointment_id,))
        conn.commit()
        messagebox.showinfo("Thành công", "Đã xóa lịch hẹn!")
        show_appointments()
    except IndexError:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn lịch hẹn để xóa!")

# Hàm xóa dữ liệu trong các ô nhập liệu
def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    service_entry.delete(0, END)

# Hàm chỉnh sửa một lịch hẹn
def edit_appointment():
    try:
        selected_item = tree.selection()[0]
        appointment_id = tree.item(selected_item)["values"][0]
        
        name_entry.delete(0, END)
        name_entry.insert(0, tree.item(selected_item)["values"][1])
        phone_entry.delete(0, END)
        phone_entry.insert(0, tree.item(selected_item)["values"][2])
        date_entry.set_date(tree.item(selected_item)["values"][3])
        service_entry.delete(0, END)
        service_entry.insert(0, tree.item(selected_item)["values"][4])
        
        def save_edits():
            appointment_date = datetime.strptime(date_entry.get(), "%Y-%m-%d")
            c.execute("UPDATE appointments SET name=%s, phone=%s, appointment_date=%s, service=%s WHERE id=%s",
                      (name_entry.get(), phone_entry.get(), appointment_date, service_entry.get(), appointment_id))
            conn.commit()
            messagebox.showinfo("Thành công", "Đã cập nhật lịch hẹn!")
            clear_entries()
            show_appointments()
            save_btn.pack_forget()
        
        save_btn = Button(main_frame, text="Lưu thay đổi", font=("Arial", 12), command=save_edits, bg="#2196F3", fg="white")
        save_btn.grid(row=5, column=1, pady=20, sticky=E)
    except IndexError:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn lịch hẹn để chỉnh sửa!")

# Hàm tìm kiếm lịch hẹn
def search_appointments():
    query = search_entry.get()
    for row in tree.get_children():
        tree.delete(row)
    c.execute("SELECT * FROM appointments WHERE name ILIKE %s", ('%' + query + '%',))
    rows = c.fetchall()
    for row in rows:
        tree.insert("", "end", values=(row[0], row[1], row[2], row[3].strftime("%Y-%m-%d"), row[4]))

# Hàm xóa tất cả lịch hẹn
def clear_all_appointments():
    confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa tất cả lịch hẹn?")
    if confirm:
        c.execute("DELETE FROM appointments")
        conn.commit()
        show_appointments()
        messagebox.showinfo("Thành công", "Đã xóa tất cả lịch hẹn!")

# Hàm thoát ứng dụng
def exit_app():
    confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát ứng dụng?")
    if confirm:
        root.destroy()

# Thiết lập giao diện
root = Tk()
root.title("Châu Gia Kiệt")
root.geometry("800x700")
root.config(bg="#e0f7fa")
# root.iconbitmap("E:/Nam_III/HK241/PythonNangCao/Python_Programming/TH/TEST/celender.ico") # Thêm icon cho trang 

# Nhãn tiêu đề
header_label = Label(root, text="Đặt Lịch Hẹn", font=("Arial", 18, "bold"), bg="#26c6da", fg="white", pady=10)
header_label.pack(fill=X)
Tooltip(header_label, "Đây là phần tiêu đề của ứng dụng đặt lịch hẹn")

# Khung chính
main_frame = Frame(root, bg="#ffffff", padx=20, pady=20)
main_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

# Các ô nhập liệu
Label(main_frame, text="Tên khách hàng:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, sticky=W, pady=5)
name_entry = Entry(main_frame, width=30, font=("Arial", 12), relief="solid", bd=1)
name_entry.grid(row=0, column=1, pady=5)
Tooltip(name_entry, "Nhập tên khách hàng")

Label(main_frame, text="Số điện thoại:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky=W, pady=5)
phone_entry = Entry(main_frame, width=30, font=("Arial", 12), relief="solid", bd=1)
phone_entry.grid(row=1, column=1, pady=5)
Tooltip(phone_entry, "Nhập số điện thoại khách hàng")

Label(main_frame, text="Chọn ngày:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky=W, pady=5)
date_entry = DateEntry(main_frame, width=28, font=("Arial", 12), date_pattern="yyyy-mm-dd", relief="solid", bd=1)
date_entry.grid(row=2, column=1, pady=5)
Tooltip(date_entry, "Chọn ngày hẹn")

Label(main_frame, text="Dịch vụ:", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, sticky=W, pady=5)
service_entry = Entry(main_frame, width=30, font=("Arial", 12), relief="solid", bd=1)
service_entry.grid(row=3, column=1, pady=5)
Tooltip(service_entry, "Nhập dịch vụ mà khách hàng yêu cầu")

# Các nút
button_frame = Frame(main_frame, bg="#ffffff")
button_frame.grid(row=4, column=0, columnspan=2, pady=20)

button_width = 12

add_btn = Button(button_frame, text="Thêm lịch hẹn", font=("Arial", 12), command=add_appointment, bg="#4CAF50", fg="white", width=button_width)
add_btn.pack(side=LEFT, padx=5)
Tooltip(add_btn, "Nhấn vào đây để thêm lịch hẹn")

edit_btn = Button(button_frame, text="Chỉnh sửa", font=("Arial", 12), command=edit_appointment, bg="#FFA726", fg="white", width=button_width)
edit_btn.pack(side=LEFT, padx=5)
Tooltip(edit_btn, "Nhấn vào đây để chỉnh sửa lịch hẹn đã chọn")

delete_btn = Button(button_frame, text="Xóa lịch hẹn", font=("Arial", 12), command=delete_appointment, bg="#f44336", fg="white", width=button_width)
delete_btn.pack(side=LEFT, padx=5)
Tooltip(delete_btn, "Nhấn vào đây để xóa lịch hẹn đã chọn")

clear_all_btn = Button(button_frame, text="Xóa tất cả", font=("Arial", 12), command=clear_all_appointments, bg="#D32F2F", fg="white", width=button_width)
clear_all_btn.pack(side=LEFT, padx=5)
Tooltip(clear_all_btn, "Nhấn vào đây để xóa tất cả lịch hẹn")

exit_btn = Button(button_frame, text="Thoát", font=("Arial", 12), command=exit_app, bg="#9E9E9E", fg="white", width=button_width)
exit_btn.pack(side=LEFT, padx=5)
Tooltip(exit_btn, "Thoát ứng dụng")

# Ô tìm kiếm
search_frame = Frame(root, bg="#ffffff")
search_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)
search_label = Label(search_frame, text="Tìm kiếm khách hàng:", font=("Arial", 12), bg="#ffffff")
search_label.pack(side=LEFT, padx=10)
search_entry = Entry(search_frame, font=("Arial", 12), width=30)
search_entry.pack(side=LEFT, padx=10)
search_btn = Button(search_frame, text="Tìm kiếm", command=search_appointments, font=("Arial", 12), bg="#00796B", fg="white")
search_btn.pack(side=LEFT, padx=10)
Tooltip(search_entry, "Nhập tên khách hàng cần tìm")

# Treeview để hiển thị danh sách lịch hẹn
tree_frame = Frame(root, bg="#ffffff")
tree_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

tree_label = Label(tree_frame, text="Danh sách lịch hẹn:", font=("Arial", 12), bg="#ffffff")
tree_label.pack(anchor=W, padx=10, pady=5)

tree = ttk.Treeview(tree_frame, columns=("ID", "Tên", "Số điện thoại", "Ngày giờ hẹn", "Dịch vụ"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Tên", text="Tên")
tree.heading("Số điện thoại", text="Số điện thoại")
tree.heading("Ngày giờ hẹn", text="Ngày hẹn")
tree.heading("Dịch vụ", text="Dịch vụ")

tree.column("ID", width=50, anchor=CENTER)
tree.column("Tên", width=150)
tree.column("Số điện thoại", width=100)
tree.column("Ngày giờ hẹn", width=150)
tree.column("Dịch vụ", width=150)

tree.pack(padx=10, pady=5, fill=BOTH, expand=True)

# Hiển thị lịch hẹn
show_appointments()
root.mainloop()
conn.close()