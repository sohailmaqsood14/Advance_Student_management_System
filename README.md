# Advanced Student Management System
## 1. Project Overview

The **Advanced Student Management System** is a Python-based command-line application designed to manage student records and academic performance efficiently.
The application allows users to add, display, search, update, and delete student information. It also provides academic calculations, student reports, filtering, sorting, and class statistics.
The project uses Object-Oriented Programming (OOP) concepts and JSON file handling to store student information permanently.

---

## 2. Project Objectives

The main objectives of this project are:
- Manage student records efficiently.
- Store student information permanently using JSON.
- Calculate academic performance automatically.
- Generate individual student reports.
- Identify top-performing students.
- Provide class and department statistics.
- Practise Python programming, OOP, functions, data structures, and file handling.

---

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| JSON | Permanent data storage |
| `json` | Reading and writing JSON data |
| `os` | File existence and file handling operations |
| VS Code | Development environment |

No external frameworks or databases are required.

---

## 4. Project Structure

The project uses a simple single-file structure.

Advance Python Project/
│
├── Student_mange.py
├── students.json
└── README.md


### File Description

- **Student_mange.py:** Contains the complete Python application, classes, methods, calculations, and command-line menu.
- **students.json:** Stores student records and their subject marks.
- **README.md:** Explains the project, its features, and execution instructions.

---

## 5. Main Features

### A. Student Management

- Add new students.
- Display all registered students.
- Search students by ID.
- Search students by name.
- Update student information.
- Delete student records.
- Prevent duplicate student IDs.
- Validate student information.

### B. Academic Management

- Calculate total marks.
- Calculate average percentage.
- Automatically assign grades.
- Determine pass or fail status.
- Generate individual student reports.
- Display passed students.
- Display failed students.
- Find the highest-performing student.
- Find the lowest-performing student.

### C. Searching, Sorting and Filtering

- Search students by ID.
- Search students by full name.
- Filter students by department.
- Filter students by grade.
- Sort students alphabetically by name.
- Sort students by average percentage.
- Display the top three students.

### D. Class Statistics

The application generates class statistics, including:

- Total registered students.
- Total passed students.
- Total failed students.
- Overall class average.
- Highest student average.
- Lowest student average.
- Grade-wise student count.
- Department-wise student count.

### E. Data Management

- Store student records in JSON format.
- Load existing records when the application starts.
- Automatically save changes after adding, updating, or deleting students.
- Handle missing and corrupted JSON files.
- Check for duplicate student IDs.

---

## 6. Academic Grading System

The application calculates student grades based on average percentage.

| Percentage | Grade | Status |
|---|---|---|
| 90–100% | A+ | Pass |
| 80–89% | A | Pass |
| 70–79% | B | Pass |
| 60–69% | C | Pass |
| Below 60% | F | Fail |

### Calculation Formulas

**Total Marks**

Total Marks = Sum of all subject marks.

**Average Percentage**

Average = (Total Marks / Maximum Possible Marks) × 100

**Pass/Fail**

- 60% or above: Pass
- Below 60%: Fail

---

## 7. Object-Oriented Programming

The project uses two main classes.

### Student Class

The `Student` class represents an individual student.

It stores:

- Student ID
- Full Name
- Age
- Email
- Department
- Subject Marks

It also contains methods to display student information.

### StudentManager Class

The `StudentManager` class manages the complete student system.

Its responsibilities include:

- Managing student records.
- Adding, updating, searching, and deleting students.
- Loading and saving JSON data.
- Calculating academic results.
- Generating reports.
- Sorting and filtering students.
- Displaying class statistics.

---

## 8. JSON Data Storage

The project uses a file named `students.json` to store student information.

Each student record contains their personal details and subject marks.

The application loads the stored records at startup and saves changes automatically when student records are modified.

This allows student information to remain available even after closing the application.

---

## 9. How to Install and Run

### Requirements

- Python 3 installed.
- Visual Studio Code or another Python editor.
- Basic knowledge of using a terminal.

### Step 1: Open the Project

Open the `Advance Python Project` folder in Visual Studio Code.

### Step 2: Open the Terminal

In VS Code, select:

`Terminal → New Terminal`

### Step 3: Run the Application

Execute the following command:

```bash
python Student_mange.py
```
If this command not work then:

Execute/Run through compiler-run sign 

### Step 4: Use the Application

The command-line menu will appear.

Enter the number corresponding to the operation you want to perform.

Follow the instructions displayed in the terminal.

---

## 10. Error Handling and Validation

The application includes basic error-handling mechanisms to improve reliability.

Examples include:

- Checking whether the JSON file exists.
- Handling corrupted JSON data.
- Preventing duplicate student IDs.
- Handling students that cannot be found.
- Checking for an empty student collection before calculating statistics.

---

## 11. Learning Outcomes

Through this project, the following Python concepts are practised:

- Variables and data types.
- Conditional statements.
- Loops.
- Functions and methods.
- Classes and objects.
- Object-Oriented Programming.
- Dictionaries and lists.
- Lambda functions.
- Sorting and filtering.
- JSON serialization and deserialization.
- File handling.
- Exception handling.
- Command-line application development.

---

## 12. Future Improvements

Possible future enhancements include:

- Exporting student reports to PDF.
- Adding more advanced input validation.
- Adding automated unit tests.
- Introducing a graphical user interface.
- Supporting additional academic subjects.
- Adding student attendance management.
- Handling project in different module not just in one file. We have to provide different files/modules to our project like student_management.py in one file and academic.py in other file and so on.

---

## 13. Author

**Project:** Advanced Student Management System  
**Language:** Python  
**Application Type:** Command-Line Application  
**Storage:** JSON File  
**Development Environment:** Visual Studio Code

---

## 14. Conclusion

The Advanced Student Management System demonstrates how Python can be used to develop a practical application for managing student information and academic performance.
It combines Object-Oriented Programming, file handling, JSON storage, data processing, and command-line interaction in one project.
 
