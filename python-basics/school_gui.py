from tkinter import *
from tkinter import ttk, messagebox
from students import Student
import openpyxl

students = []

# ================= LOGIN WINDOW =================
def login():
    if username.get() == "admin" and password.get() == "1234":
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror("Login Failed", "Wrong Username or Password")


login_window = Tk()
login_window.title("Login")
login_window.geometry("400x300")
login_window.configure(bg="#0f0f1a")

Label(login_window, text="SCHOOL LOGIN",
      bg="#0f0f1a", fg="#00ffcc",
      font=("Arial", 18, "bold")).pack(pady=20)

username = Entry(login_window)
username.pack(pady=10)
username.insert(0, "admin")

password = Entry(login_window, show="*")
password.pack(pady=10)

Button(login_window, text="Login",
       bg="#00ffcc", fg="black",
       command=login).pack(pady=20)

# ================= MAIN WINDOW =================
def main_window():
    root = Tk()
    root.title("Advanced School Management System")
    root.geometry("1000x650")
    root.configure(bg="#0f0f1a")

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="#1a1a2e",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#1a1a2e")

    style.map("Treeview",
              background=[("selected", "#00ffcc")])

    # ---------- FUNCTIONS ----------
    def register_student():
        if id_entry.get() == "" or name_entry.get() == "":
            messagebox.showerror("Error", "Fill all required fields")
            return

        student = Student(id_entry.get(),
                          name_entry.get(),
                          course_entry.get(),
                          phone_entry.get())
        students.append(student)
        update_table()
        update_dashboard()
        clear_fields()

    def update_table():
        table.delete(*table.get_children())
        for s in students:
            table.insert("", END, values=s.display())

    def assign_course():
        selected = table.focus()
        if not selected:
            return
        values = table.item(selected, "values")
        for s in students:
            if s.student_id == values[0]:
                s.assign_course_grade(course_entry.get(),
                                      grade_entry.get())
        update_table()

    def delete_student():
        selected = table.focus()
        if not selected:
            return
        values = table.item(selected, "values")
        for s in students:
            if s.student_id == values[0]:
                students.remove(s)
                break
        update_table()
        update_dashboard()

    def search_student():
        search_id = search_entry.get()
        table.delete(*table.get_children())
        for s in students:
            if s.student_id == search_id:
                table.insert("", END, values=s.display())

    def save_excel():
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["ID", "Name", "Course", "Phone", "Grade"])
        for s in students:
            sheet.append(s.display())
        workbook.save("students.xlsx")
        messagebox.showinfo("Saved", "Saved to Excel")

    def clear_fields():
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        course_entry.delete(0, END)
        phone_entry.delete(0, END)
        grade_entry.delete(0, END)

    def update_dashboard():
        total_label.config(text=f"Total Students: {len(students)}")

    # ---------- TITLE ----------
    Label(root,
          text="ADVANCED SCHOOL MANAGEMENT SYSTEM",
          bg="#0f0f1a",
          fg="#00ffcc",
          font=("Arial", 22, "bold")).pack(pady=10)

    # ---------- DASHBOARD ----------
    total_label = Label(root,
                        text="Total Students: 0",
                        bg="#0f0f1a",
                        fg="white",
                        font=("Arial", 14))
    total_label.pack()

    # ---------- FORM ----------
    form = Frame(root, bg="#0f0f1a")
    form.pack(pady=10)

    labels = ["ID", "Name", "Course", "Phone", "Grade"]
    entries = []

    for i, text in enumerate(labels):
        Label(form, text=text,
              bg="#0f0f1a",
              fg="white").grid(row=i, column=0, padx=5, pady=5)
        entry = Entry(form)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    id_entry, name_entry, course_entry, phone_entry, grade_entry = entries

    # ---------- BUTTONS ----------
    btn_frame = Frame(root, bg="#0f0f1a")
    btn_frame.pack(pady=10)

    Button(btn_frame, text="Register",
           bg="#00ffcc", width=12,
           command=register_student).grid(row=0, column=0, padx=5)

    Button(btn_frame, text="Assign",
           bg="#0099ff", width=12,
           command=assign_course).grid(row=0, column=1, padx=5)

    Button(btn_frame, text="Delete",
           bg="#ff4d4d", width=12,
           command=delete_student).grid(row=0, column=2, padx=5)

    Button(btn_frame, text="Save Excel",
           bg="#ffaa00", width=12,
           command=save_excel).grid(row=0, column=3, padx=5)

    # ---------- SEARCH ----------
    search_frame = Frame(root, bg="#0f0f1a")
    search_frame.pack()

    search_entry = Entry(search_frame)
    search_entry.grid(row=0, column=0)

    Button(search_frame, text="Search by ID",
           bg="#00ffcc",
           command=search_student).grid(row=0, column=1)

    # ---------- TABLE ----------
    table = ttk.Treeview(root,
                         columns=("ID", "Name", "Course", "Phone", "Grade"),
                         show="headings")

    for col in ("ID", "Name", "Course", "Phone", "Grade"):
        table.heading(col, text=col)
        table.column(col, width=160)

    table.pack(pady=20)

    root.mainloop()


login_window.mainloop()