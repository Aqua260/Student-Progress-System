🎓 Student Progress Tracker
📘 Overview

The Student Progress Tracker is a desktop application developed using Python (Tkinter GUI) and MySQL database.
It allows teachers or administrators to record, manage, and analyze students’ academic performance and attendance efficiently.
This project helps in tracking student data digitally with options to add, update, view, and delete records.

⚙️ Features

➕ Add New Student Record — Easily insert details like name, roll number, subject, marks, attendance, and remarks.

✏️ Update Student Details — Modify marks, attendance percentage, or remarks when needed.

❌ Delete Records — Remove student data securely.

📋 View All Records — Display stored data in a tabular Treeview format.

🔒 Database Integration — Data stored persistently in a MySQL database (student_db).

🧠 User-Friendly Interface — Built using Tkinter for a simple, interactive GUI experience.

🛠️ Technologies Used

Python 3

Tkinter — For GUI interface

MySQL — For database storage

MySQL Connector for Python

🗃️ Database Structure

Database Name: student_db
Table Name: students

Column Name	Data Type	Description
id	INT (Primary Key, Auto Increment)	Unique Student ID
name	VARCHAR(100)	Student Name
roll_no	VARCHAR(50)	Roll Number
subject	VARCHAR(100)	Subject Name
marks	INT	Marks Obtained
attendance	INT	Attendance Percentage
remarks	VARCHAR(255)	Remarks about student performance
🚀 How to Run the Project

Install Dependencies

pip install mysql-connector-python


Create MySQL Database

CREATE DATABASE student_db;
USE student_db;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll_no VARCHAR(50),
    subject VARCHAR(100),
    marks INT,
    attendance INT,
    remarks VARCHAR(255)
);


Update Database Credentials
Open the Python file (student_progress_tracker.py) and set your MySQL username and password:

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # update if your MySQL has a password
    database="student_db"
)


Run the Application

python student_progress_tracker.py


The Tkinter window will open — start adding, viewing, and managing student records!

📈 Future Enhancements

Export student reports to PDF or Excel

Add search and filter options

Include graphical analytics (charts of marks/attendance trends)

Implement login authentication for teachers

👩‍💻 Author

Purnima Aggarwal
MCA Student | Developer | Tech Enthusiast

🏷️ License

This project is for educational purposes only and can be used for academic learning or college submissions.
