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

# Đoạn mã tạo bảng đã được ẩn đi vì bảng đã có sẵn
# c.execute('''CREATE TABLE IF NOT EXISTS appointments (
#                 id SERIAL PRIMARY KEY,
#                 name VARCHAR(100),
#                 phone VARCHAR(15),
#                 appointment_date TIMESTAMP,
#                 service VARCHAR(100))''')
# conn.commit()

# Hàm thêm lịch hẹn
def add_appointment():
    # Kiểm tra nếu các trường còn trống
    if name_entry.get() == "" or phone_entry.get() == "" or service_entry.get() == "":
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
    else:
        try:
            # Lấy ngày hẹn từ người dùng
            appointment_date = datetime.strptime(date_entry.get(), "%Y-%m-%d")
            # Thêm dữ liệu vào bảng
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
    # Xóa dữ liệu cũ trong treeview
    for row in tree.get_children():
        tree.delete(row)
    # Truy vấn dữ liệu từ bảng và hiển thị
    c.execute("SELECT * FROM appointments")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", "end", values=(row[0], row[1], row[2], row[3].strftime("%Y-%m-%d"), row[4]))

# Hàm xóa một lịch hẹn
def delete_appointment():
    try:
        # Lấy lịch hẹn đã chọn trong treeview
        selected_item = tree.selection()[0]
        appointment_id = tree.item(selected_item)["values"][0]
        # Xóa lịch hẹn từ cơ sở dữ liệu
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
        # Lấy lịch hẹn đã chọn trong treeview
        selected_item = tree.selection()[0]
        appointment_id = tree.item(selected_item)["values"][0]
        
        # Điền dữ liệu lịch hẹn vào các ô nhập liệu
        name_entry.delete(0, END)
        name_entry.insert(0, tree.item(selected_item)["values"][1])
        phone_entry.delete(0, END)
        phone_entry.insert(0, tree.item(selected_item)["values"][2])
        date_entry.set_date(tree.item(selected_item)["values"][3])
        service_entry.delete(0, END)
        service_entry.insert(0, tree.item(selected_item)["values"][4])
        
        # Nút lưu thay đổi
        def save_edits():
            appointment_date = datetime.strptime(date_entry.get(), "%Y-%m-%d")
            # Cập nhật dữ liệu trong cơ sở dữ liệu
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
    # Tìm kiếm tên khách hàng trong bảng
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
root.title("Ứng dụng Đặt lịch hẹn")
root.geometry("800x700")
root.config(bg="#e0f7fa")

# Nhãn tiêu đề
header_label = Label(root, text="Lịch Hẹn", font=("Arial", 18, "bold"), bg="#26c6da", fg="white", pady=10)
header_label.pack(fill=X)

# Khung chính
main_frame = Frame(root, bg="#ffffff", padx=20, pady=20)
main_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

# Các ô nhập liệu
Label(main_frame, text="Tên khách hàng:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, sticky=W, pady=5)
name_entry = Entry(main_frame, width=30, font=("Arial", 12), relief="solid", bd=1)
name_entry.grid(row=0, column=1, pady=5)

Label(main_frame, text="Số điện thoại:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky=W, pady=5)
phone_entry = Entry(main_frame, width=30, font=("Arial", 12), relief="solid", bd=1)
phone_entry.grid(row=1, column=1, pady=5)

Label(main_frame, text="Chọn ngày:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky=W, pady=5)
date_entry = DateEntry(main_frame, width=28, font=("Arial", 12), date_pattern="yyyy-mm-dd", relief="solid", bd=1)
date_entry.grid(row=2, column=1, pady=5)

Label(main_frame, text="Dịch vụ:", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, sticky=W, pady=5)
service_entry = Entry(main_frame, width=30, font=("Arial", 12), relief="solid", bd=1)
service_entry.grid(row=3, column=1, pady=5)

# Các nút
button_frame = Frame(main_frame, bg="#ffffff")
button_frame.grid(row=4, column=0, columnspan=2, pady=20)

# Điều chỉnh độ rộng nút cho vừa khung hình
button_width = 12

add_btn = Button(button_frame, text="Thêm lịch hẹn", font=("Arial", 12), command=add_appointment, bg="#4CAF50", fg="white", width=button_width)
add_btn.pack(side=LEFT, padx=5)

edit_btn = Button(button_frame, text="Chỉnh sửa", font=("Arial", 12), command=edit_appointment, bg="#FFA726", fg="white", width=button_width)
edit_btn.pack(side=LEFT, padx=5)

delete_btn = Button(button_frame, text="Xóa lịch hẹn", font=("Arial", 12), command=delete_appointment, bg="#f44336", fg="white", width=button_width)
delete_btn.pack(side=LEFT, padx=5)

clear_all_btn = Button(button_frame, text="Xóa tất cả", font=("Arial", 12), command=clear_all_appointments, bg="#D32F2F", fg="white", width=button_width)
clear_all_btn.pack(side=LEFT, padx=5)

# Nút Thoát
exit_btn = Button(button_frame, text="Thoát", font=("Arial", 12), command=exit_app, bg="#9E9E9E", fg="white", width=button_width)
exit_btn.pack(side=LEFT, padx=5)

# Ô tìm kiếm
search_frame = Frame(root, bg="#ffffff")
search_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)
search_label = Label(search_frame, text="Tìm kiếm khách hàng:", font=("Arial", 12), bg="#ffffff")
search_label.pack(side=LEFT, padx=10)
search_entry = Entry(search_frame, font=("Arial", 12), width=30)
search_entry.pack(side=LEFT, padx=10)
search_btn = Button(search_frame, text="Tìm kiếm", command=search_appointments, font=("Arial", 12), bg="#00796B", fg="white")
search_btn.pack(side=LEFT, padx=10)

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

# Đặt kích thước cột
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