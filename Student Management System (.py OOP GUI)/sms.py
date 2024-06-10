import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")

        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=1)

        # Create frames for each tab
        self.create_student_management_tab()
        self.create_attendance_tracking_tab()
        self.create_grade_book_tab()
        self.create_health_info_tab()
        self.create_billing_records_tab()

        # Load data from files
        self.load_data()

    def load_data(self):
        self.load_students()
        self.load_attendance()
        self.load_grades()
        self.load_health_info()
        self.load_billing()

    def load_students(self):
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name, dob, address, contact = line.strip().split(",")
                self.student_table.insert("", tk.END, values=(student_id, name, dob, address, contact))

    def load_attendance(self):
        with open("attendance.txt", "r") as file:
            for line in file:
                student_id, date, attendance = line.strip().split(",")
                self.attendance_table.insert("", tk.END, values=(student_id, date, attendance))

    def load_grades(self):
        with open("grades.txt", "r") as file:
            for line in file:
                student_id, subject, grade = line.strip().split(",")
                self.grade_table.insert("", tk.END, values=(student_id, subject, grade))

    def load_health_info(self):
        with open("health_info.txt", "r") as file:
            for line in file:
                student_id, condition, emergency_contact, immunization = line.strip().split(",")
                self.health_table.insert("", tk.END, values=(student_id, condition, emergency_contact, immunization))

    def load_billing(self):
        with open("billing.txt", "r") as file:
            for line in file:
                student_id, payment_details, outstanding_fees, payment_history = line.strip().split(",")
                self.billing_table.insert("", tk.END, values=(student_id, payment_details, outstanding_fees, payment_history))

    def save_students(self):
        with open("students.txt", "w") as file:
            for item in self.student_table.get_children():
                student = self.student_table.item(item)["values"]
                file.write(",".join(student) + "\n")

    def save_attendance(self):
        with open("attendance.txt", "w") as file:
            for item in self.attendance_table.get_children():
                attendance = self.attendance_table.item(item)["values"]
                file.write(",".join(attendance) + "\n")

    def save_grades(self):
        with open("grades.txt", "w") as file:
            for item in self.grade_table.get_children():
                grade = self.grade_table.item(item)["values"]
                file.write(",".join(grade) + "\n")

    def save_health_info(self):
        with open("health_info.txt", "w") as file:
            for item in self.health_table.get_children():
                health_info = self.health_table.item(item)["values"]
                file.write(",".join(health_info) + "\n")

    def save_billing(self):
        with open("billing.txt", "w") as file:
            for item in self.billing_table.get_children():
                billing = self.billing_table.item(item)["values"]
                file.write(",".join(billing) + "\n")

    def create_student_management_tab(self):
        self.student_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.student_frame, text="Student Records")

        # Add widgets to the student_frame
        self.student_table = ttk.Treeview(self.student_frame, columns=("id", "name", "dob", "address", "contact"), show="headings")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("contact", text="Contact")
        self.student_table.pack(fill=tk.BOTH, expand=1)

        # Add buttons for adding, editing, deleting, and searching student records
        button_frame = ttk.Frame(self.student_frame)
        button_frame.pack(fill=tk.X)
        ttk.Button(button_frame, text="Add", command=self.add_student).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Edit", command=self.edit_student).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Delete", command=self.delete_student).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Search", command=self.search_student).pack(side=tk.LEFT)

    def create_attendance_tracking_tab(self):
        self.attendance_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.attendance_frame, text="Attendance Tracking")

        tk.Label(self.attendance_frame, text="Select Date:").pack()
        self.attendance_date = tk.Entry(self.attendance_frame)
        self.attendance_date.pack()

        self.attendance_table = ttk.Treeview(self.attendance_frame, columns=("id", "date", "attendance"), show="headings")
        self.attendance_table.heading("id", text="Student ID")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("attendance", text="Attendance")
        self.attendance_table.pack(fill=tk.BOTH, expand=1)

        button_frame = ttk.Frame(self.attendance_frame)
        button_frame.pack(fill=tk.X)
        ttk.Button(button_frame, text="Mark Present", command=self.mark_present).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Mark Absent", command=self.mark_absent).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Save Attendance", command=self.save_attendance).pack(side=tk.LEFT)

    def create_grade_book_tab(self):
        self.grade_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.grade_frame, text="Grade Book")

        self.grade_table = ttk.Treeview(self.grade_frame, columns=("id", "subject", "grade"), show="headings")
        self.grade_table.heading("id", text="Student ID")
        self.grade_table.heading("subject", text="Subject")
        self.grade_table.heading("grade", text="Grade")
        self.grade_table.pack(fill=tk.BOTH, expand=1)

        button_frame = ttk.Frame(self.grade_frame)
        button_frame.pack(fill=tk.X)
        ttk.Button(button_frame, text="Add Grade", command=self.add_grade).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Edit Grade", command=self.edit_grade).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Delete Grade", command=self.delete_grade).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Save Grades", command=self.save_grades).pack(side=tk.LEFT)

    def create_health_info_tab(self):
        self.health_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.health_frame, text="Health Information")

        self.health_table = ttk.Treeview(self.health_frame, columns=("id", "condition", "emergency_contact", "immunization"), show="headings")
        self.health_table.heading("id", text="Student ID")
        self.health_table.heading("condition", text="Health Condition")
        self.health_table.heading("emergency_contact", text="Emergency Contact")
        self.health_table.heading("immunization", text="Immunization Record")
        self.health_table.pack(fill=tk.BOTH, expand=1)

        button_frame = ttk.Frame(self.health_frame)
        button_frame.pack(fill=tk.X)
        ttk.Button(button_frame, text="Add Health Info", command=self.add_health_info).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Edit Health Info", command=self.edit_health_info).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Delete Health Info", command=self.delete_health_info).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Save Health Info", command=self.save_health_info).pack(side=tk.LEFT)

    def create_billing_records_tab(self):
        self.billing_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.billing_frame, text="Billing Records")

        self.billing_table = ttk.Treeview(self.billing_frame, columns=("id", "payment_details", "outstanding_fees", "payment_history"), show="headings")
        self.billing_table.heading("id", text="Student ID")
        self.billing_table.heading("payment_details", text="Payment Details")
        self.billing_table.heading("outstanding_fees", text="Outstanding Fees")
        self.billing_table.heading("payment_history", text="Payment History")
        self.billing_table.pack(fill=tk.BOTH, expand=1)

        button_frame = ttk.Frame(self.billing_frame)
        button_frame.pack(fill=tk.X)
        ttk.Button(button_frame, text="Add Payment", command=self.add_payment).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Edit Payment", command=self.edit_payment).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Delete Payment", command=self.delete_payment).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Save Payments", command=self.save_billing).pack(side=tk.LEFT)

    def add_student(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Student")

        tk.Label(add_window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(add_window)
        student_id_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Date of Birth:").grid(row=2, column=0)
        dob_entry = tk.Entry(add_window)
        dob_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Address:").grid(row=3, column=0)
        address_entry = tk.Entry(add_window)
        address_entry.grid(row=3, column=1)

        tk.Label(add_window, text="Contact:").grid(row=4, column=0)
        contact_entry = tk.Entry(add_window)
        contact_entry.grid(row=4, column=1)

        def save_student():
            student_id = student_id_entry.get()
            name = name_entry.get()
            dob = dob_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            self.student_table.insert("", tk.END, values=(student_id, name, dob, address, contact))
            add_window.destroy()
            self.save_students()

        tk.Button(add_window, text="Save", command=save_student).grid(row=5, column=0, columnspan=2)

    def edit_student(self):
        selected_item = self.student_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No student selected")
            return

        item = self.student_table.item(selected_item)
        student_data = item["values"]

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Student")

        tk.Label(edit_window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(edit_window)
        student_id_entry.insert(0, student_data[0])
        student_id_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, student_data[1])
        name_entry.grid(row=1, column=1)

        tk.Label(edit_window, text="Date of Birth:").grid(row=2, column=0)
        dob_entry = tk.Entry(edit_window)
        dob_entry.insert(0, student_data[2])
        dob_entry.grid(row=2, column=1)

        tk.Label(edit_window, text="Address:").grid(row=3, column=0)
        address_entry = tk.Entry(edit_window)
        address_entry.insert(0, student_data[3])
        address_entry.grid(row=3, column=1)

        tk.Label(edit_window, text="Contact:").grid(row=4, column=0)
        contact_entry = tk.Entry(edit_window)
        contact_entry.insert(0, student_data[4])
        contact_entry.grid(row=4, column=1)

        def save_changes():
            self.student_table.item(selected_item, values=(student_id_entry.get(), name_entry.get(), dob_entry.get(), address_entry.get(), contact_entry.get()))
            edit_window.destroy()
            self.save_students()

        tk.Button(edit_window, text="Save", command=save_changes).grid(row=5, column=0, columnspan=2)

    def delete_student(self):
        selected_item = self.student_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No student selected")
            return

        self.student_table.delete(selected_item)
        self.save_students()

    def search_student(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Student")

        tk.Label(search_window, text="Search by Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(search_window)
        student_id_entry.grid(row=0, column=1)

        def search():
            student_id = student_id_entry.get()
            found = False
            for item in self.student_table.get_children():
                student = self.student_table.item(item)["values"]
                if student_id == student[0]:
                    self.student_table.selection_set(item)
                    self.student_table.see(item)
                    found = True
                    break
            if not found:
                messagebox.showinfo("Info", "No student found with the given ID")

        tk.Button(search_window, text="Search", command=search).grid(row=1, column=0, columnspan=2)

    
    def add_grade(self):
        grade_window = tk.Toplevel(self.root)
        grade_window.title("Add Grade")

        tk.Label(grade_window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(grade_window)
        student_id_entry.grid(row=0, column=1)

        tk.Label(grade_window, text="Subject:").grid(row=1, column=0)
        subject_entry = tk.Entry(grade_window)
        subject_entry.grid(row=1, column=1)

        tk.Label(grade_window, text="Grade:").grid(row=2, column=0)
        grade_entry = tk.Entry(grade_window)
        grade_entry.grid(row=2, column=1)

        def save_grade():
            student_id = student_id_entry.get()
            subject = subject_entry.get()
            grade = grade_entry.get()
            self.grade_table.insert("", tk.END, values=(student_id, subject, grade))
            grade_window.destroy()
            self.save_grades()

        tk.Button(grade_window, text="Save", command=save_grade).grid(row=3, column=0, columnspan=2)

    def edit_grade(self):
        selected_item = self.grade_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No grade selected")
            return

        item = self.grade_table.item(selected_item)
        grade_data = item["values"]

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Grade")

        tk.Label(edit_window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(edit_window)
        student_id_entry.insert(0, grade_data[0])
        student_id_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="Subject:").grid(row=1, column=0)
        subject_entry = tk.Entry(edit_window)
        subject_entry.insert(0, grade_data[1])
        subject_entry.grid(row=1, column=1)

        tk.Label(edit_window, text="Grade:").grid(row=2, column=0)
        grade_entry = tk.Entry(edit_window)
        grade_entry.insert(0, grade_data[2])
        grade_entry.grid(row=2, column=1)

        def save_changes():
            self.grade_table.item(selected_item, values=(student_id_entry.get(), subject_entry.get(), grade_entry.get()))
            edit_window.destroy()
            self.save_grades()

        tk.Button(edit_window, text="Save", command=save_changes).grid(row=3, column=0, columnspan=2)

    def delete_grade(self):
        selected_item = self.grade_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No grade selected")
            return

        self.grade_table.delete(selected_item)
        self.save_grades()

    def mark_present(self):
        selected_item = self.attendance_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No student selected")
            return
        self.attendance_table.set(selected_item, column="attendance", value="Present")
        self.save_attendance()

    def mark_absent(self):
        selected_item = self.attendance_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No student selected")
            return
        self.attendance_table.set(selected_item, column="attendance", value="Absent")
        self.save_attendance()

    def add_health_info(self):
        health_window = tk.Toplevel(self.root)
        health_window.title("Add Health Information")

        tk.Label(health_window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(health_window)
        student_id_entry.grid(row=0, column=1)

        tk.Label(health_window, text="Health Condition:").grid(row=1, column=0)
        condition_entry = tk.Entry(health_window)
        condition_entry.grid(row=1, column=1)

        tk.Label(health_window, text="Emergency Contact:").grid(row=2, column=0)
        emergency_contact_entry = tk.Entry(health_window)
        emergency_contact_entry.grid(row=2, column=1)

        tk.Label(health_window, text="Immunization Record:").grid(row=3, column=0)
        immunization_entry = tk.Entry(health_window)
        immunization_entry.grid(row=3, column=1)

        def save_health_info():
            student_id = student_id_entry.get()
            condition = condition_entry.get()
            emergency_contact = emergency_contact_entry.get()
            immunization = immunization_entry.get()
            self.health_table.insert("", tk.END, values=(student_id, condition, emergency_contact, immunization))
            health_window.destroy()
            self.save_health_info()

        tk.Button(health_window, text="Save", command=save_health_info).grid(row=4, column=0, columnspan=2)

    def edit_health_info(self):
        selected_item = self.health_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No health information selected")
            return

        item = self.health_table.item(selected_item)
        health_data = item["values"]

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Health Information")

        tk.Label(edit_window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(edit_window)
        student_id_entry.insert(0, health_data[0])
        student_id_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="Health Condition:").grid(row=1, column=0)
        condition_entry = tk.Entry(edit_window)
        condition_entry.insert(0, health_data[1])
        condition_entry.grid(row=1, column=1)

        tk.Label(edit_window, text="Emergency Contact:").grid(row=2, column=0)
        emergency_contact_entry = tk.Entry(edit_window)
        emergency_contact_entry.insert(0, health_data[2])
        emergency_contact_entry.grid(row=2, column=1)

        tk.Label(edit_window, text="Immunization Record:").grid(row=3, column=0)
        immunization_entry = tk.Entry(edit_window)
        immunization_entry.insert(0, health_data[3])
        immunization_entry.grid(row=3, column=1)

        def save_changes():
            self.health_table.item(selected_item, values=(student_id_entry.get(), condition_entry.get(), emergency_contact_entry.get(), immunization_entry.get()))
            edit_window.destroy()
            self.save_health_info()

        tk.Button(edit_window, text="Save", command=save_changes).grid(row=4, column=0, columnspan=2)

    def delete_health_info(self):
        selected_item = self.health_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No health information selected")
            return

        self.health_table.delete(selected_item)
        self.save_health_info()

    def add_payment(self):
        payment_window = tk.Toplevel(self.root)
        payment_window.title("Add Payment")

        tk.Label(payment_window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(payment_window)
        student_id_entry.grid(row=0, column=1)

        tk.Label(payment_window, text="Payment Details:").grid(row=1, column=0)
        payment_details_entry = tk.Entry(payment_window)
        payment_details_entry.grid(row=1, column=1)

        tk.Label(payment_window, text="Outstanding Fees:").grid(row=2, column=0)
        outstanding_fees_entry = tk.Entry(payment_window)
        outstanding_fees_entry.grid(row=2, column=1)

        tk.Label(payment_window, text="Payment History:").grid(row=3, column=0)
        payment_history_entry = tk.Entry(payment_window)
        payment_history_entry.grid(row=3, column=1)

        def save_payment():
            student_id = student_id_entry.get()
            payment_details = payment_details_entry.get()
            outstanding_fees = outstanding_fees_entry.get()
            payment_history = payment_history_entry.get()
            self.billing_table.insert("", tk.END, values=(student_id, payment_details, outstanding_fees, payment_history))
            payment_window.destroy()
            self.save_billing()

        tk.Button(payment_window, text="Save", command=save_payment).grid(row=4, column=0, columnspan=2)

    def edit_payment(self):
        selected_item = self.billing_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No payment selected")
            return

        item = self.billing_table.item(selected_item)
        payment_data = item["values"]

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Payment")

        tk.Label(edit_window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(edit_window)
        student_id_entry.insert(0, payment_data[0])
        student_id_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="Payment Details:").grid(row=1, column=0)
        payment_details_entry = tk.Entry(edit_window)
        payment_details_entry.insert(0, payment_data[1])
        payment_details_entry.grid(row=1, column=1)

        tk.Label(edit_window, text="Outstanding Fees:").grid(row=2, column=0)
        outstanding_fees_entry = tk.Entry(edit_window)
        outstanding_fees_entry.insert(0, payment_data[2])
        outstanding_fees_entry.grid(row=2, column=1)

        tk.Label(edit_window, text="Payment History:").grid(row=3, column=0)
        payment_history_entry = tk.Entry(edit_window)
        payment_history_entry.insert(0, payment_data[3])
        payment_history_entry.grid(row=3, column=1)

        def save_changes():
            self.billing_table.item(selected_item, values=(student_id_entry.get(), payment_details_entry.get(), outstanding_fees_entry.get(), payment_history_entry.get()))
            edit_window.destroy()
            self.save_billing()

        tk.Button(edit_window, text="Save", command=save_changes).grid(row=4, column=0, columnspan=2)

    def delete_payment(self):
        selected_item = self.billing_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No payment selected")
            return

        self.billing_table.delete(selected_item)
        self.save_billing()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
