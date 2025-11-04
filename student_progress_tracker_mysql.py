import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox

# ------------------ DATABASE CONNECTION ------------------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # leave empty if no password is set in XAMPP
        database="student_db"
    )
    cursor = conn.cursor()
    print("✅ Database connected successfully!")

except mysql.connector.Error as err:
    print("❌ Database connection failed:", err)
    exit()

# ------------------ FUNCTIONS ------------------
def add_student():
    name = entry_name.get()
    roll = entry_roll.get()
    subject = entry_subject.get()
    marks = entry_marks.get()
    attendance = entry_attendance.get()
    remarks = entry_remarks.get()

    if name == "" or roll == "":
        messagebox.showwarning("Input Error", "Please fill all required fields")
        return

    try:
        cursor.execute(
            "INSERT INTO students (name, roll_no, subject, marks, attendance, remarks) VALUES (%s, %s, %s, %s, %s, %s)",
            (name, roll, subject, marks, attendance, remarks)
        )
        conn.commit()
        messagebox.showinfo("Success", "Record Added Successfully!")
        clear_fields()
        show_records()
    except Exception as e:
        messagebox.showerror("Error", f"Error inserting record: {e}")

def clear_fields():
    entry_name.delete(0, END)
    entry_roll.delete(0, END)
    entry_subject.delete(0, END)
    entry_marks.delete(0, END)
    entry_attendance.delete(0, END)
    entry_remarks.delete(0, END)

def show_records():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", END, values=row)

def delete_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select Record", "Please select a record to delete")
        return
    item = tree.item(selected[0])
    student_id = item['values'][0]

    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    messagebox.showinfo("Deleted", "Record deleted successfully!")
    show_records()

def update_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select Record", "Please select a record to update")
        return
    item = tree.item(selected[0])
    student_id = item['values'][0]
    updated_marks = entry_marks.get()
    updated_attendance = entry_attendance.get()
    updated_remarks = entry_remarks.get()

    cursor.execute(
        "UPDATE students SET marks=%s, attendance=%s, remarks=%s WHERE id=%s",
        (updated_marks, updated_attendance, updated_remarks, student_id)
    )
    conn.commit()
    messagebox.showinfo("Updated", "Record updated successfully!")
    show_records()

# ------------------ UI SETUP ------------------
root = Tk()
root.title("🎓 Student Progress Tracker (MySQL Version)")
root.geometry("900x600")
root.config(bg="#f0f4f7")

Label(root, text="Student Progress Tracker", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#2c3e50").pack(pady=10)

frame = Frame(root, bg="#f0f4f7")
frame.pack()

Label(frame, text="Name:", bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5)
entry_name = Entry(frame, width=20)
entry_name.grid(row=0, column=1)

Label(frame, text="Roll No:", bg="#f0f4f7").grid(row=0, column=2, padx=5, pady=5)
entry_roll = Entry(frame, width=20)
entry_roll.grid(row=0, column=3)

Label(frame, text="Subject:", bg="#f0f4f7").grid(row=1, column=0, padx=5, pady=5)
entry_subject = Entry(frame, width=20)
entry_subject.grid(row=1, column=1)

Label(frame, text="Marks:", bg="#f0f4f7").grid(row=1, column=2, padx=5, pady=5)
entry_marks = Entry(frame, width=20)
entry_marks.grid(row=1, column=3)

Label(frame, text="Attendance (%):", bg="#f0f4f7").grid(row=2, column=0, padx=5, pady=5)
entry_attendance = Entry(frame, width=20)
entry_attendance.grid(row=2, column=1)

Label(frame, text="Remarks:", bg="#f0f4f7").grid(row=2, column=2, padx=5, pady=5)
entry_remarks = Entry(frame, width=20)
entry_remarks.grid(row=2, column=3)

# Buttons
Button(frame, text="Add Record", command=add_student, bg="#27ae60", fg="white", width=15).grid(row=3, column=0, pady=10)
Button(frame, text="Update Record", command=update_record, bg="#2980b9", fg="white", width=15).grid(row=3, column=1)
Button(frame, text="Delete Record", command=delete_record, bg="#c0392b", fg="white", width=15).grid(row=3, column=2)
Button(frame, text="Clear Fields", command=clear_fields, bg="#7f8c8d", fg="white", width=15).grid(row=3, column=3)

# Table
columns = ("ID", "Name", "Roll No", "Subject", "Marks", "Attendance", "Remarks")
tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=CENTER, width=120)
tree.pack(pady=20)

show_records()

root.mainloop()
