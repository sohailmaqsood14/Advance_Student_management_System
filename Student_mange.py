import json
import os

class Student:

    def __init__(self, student_id, name, age, email, department, marks):

        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department
        self.marks = marks

    def display_student(self):

        print("\n STUDENT DETAILS ")

        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Department:", self.department)

        print("\n Subject Marks: ")

        for subject, mark in self.marks.items():
            print(subject, ":", mark)

        print("________________________________")

# STUDENT MANAGEMENT SYSTEM
class StudentManager:

    def __init__(self):

        self.students = {}

        self.filename = "students.json"

        self.load_data()

    # LOAD JSON DATA
    def load_data(self):

        if not os.path.exists(self.filename):

            self.save_data()
            return

        try:

            with open(self.filename, "r") as file:

                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("Invalid student data format")

            for student_id, details in data.items():

                if not isinstance(details, dict):
                    raise ValueError("Invalid student record")

                required_fields = [
                    "student_id", "name", "age",
                    "email", "department", "marks"
                ]

                if not all(field in details for field in required_fields):
                    raise ValueError("Incomplete student record")

                if not isinstance(details["marks"], dict):
                    raise ValueError("Invalid marks data")

                if str(student_id) != str(details["student_id"]):
                    raise ValueError("Student ID mismatch")

                self.students[str(student_id)] = Student(
                    str(student_id),
                    details["name"],
                    details["age"],
                    details["email"],
                    details["department"],
                    details["marks"]
                )

            print("Student records loaded successfully!")

        except (json.JSONDecodeError, ValueError, TypeError, OSError) as error:

            print("Error loading student data:", error)
            print("Starting with an empty student list.")

            self.students = {}

    # SAVE JSON DATA

    def save_data(self):

        data = {}

        for student_id, student in self.students.items():

            data[student_id] = {

                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "email": student.email,
                "department": student.department,
                "marks": student.marks

            }

        try:

            with open(self.filename, "w") as file:

                json.dump(data, file, indent=4)

            print("Data saved successfully!")

        except (OSError, TypeError, ValueError) as error:

            print("Error saving data:", error)

    # ADD STUDENT

    def add_student(self):

        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty!")
            return

        if student_id in self.students:

            print("Student ID already exists!")
            return

        name = input("Enter Full Name: ").strip()

        if not name or not all(part.isalpha() for part in name.split()):
            print("Invalid name!")
            return

        try:

            age = int(input("Enter Age: "))

            if age <= 0 or age > 60:

                print("Invalid age!")
                return

        except ValueError:

            print("Age must be a number!")
            return

        email = input("Enter Email: ").strip()

        if "@" not in email or "." not in email:
            print("Invalid email!")
            return

        department = input("Enter Department: ").strip()

        if not department:
            print("Department cannot be empty!")
            return

        marks = {}

        subjects = [
            "Python",
            "Database",
            "Mathematics",
            "English",
            "Programming"
        ]

        for subject in subjects:

            try:

                mark = float(input(f"Enter {subject} Marks: "))

                if mark < 0 or mark > 100:

                    print("Marks must be between 0 and 100!")
                    return

                marks[subject] = mark

            except ValueError:

                print("Invalid marks!")
                return

        student = Student(
            student_id,
            name,
            age,
            email,
            department,
            marks
        )

        self.students[student_id] = student

        self.save_data()

        print("Student added successfully!")

    # DISPLAY STUDENTS
    def display_students(self):

        if not self.students:

            print("No students registered!")
            return

        for student in self.students.values():

            student.display_student()

    # SEARCH STUDENT
 
    def search_student(self):

        print("\n 1. Search by ID")
        print("2. Search by Name")

        choice = input("Enter choice: ")

        if choice == "1":

            student_id = input("Enter Student ID: ").strip()

            student = self.students.get(student_id)

            if student:
                student.display_student()

            else:
                print("Student not found!")

        elif choice == "2":

            name = input("Enter Student Name: ").strip().lower()

            found = False

            for student in self.students.values():

                if student.name.lower() == name:

                    student.display_student()
                    found = True

            if not found:
                print("Student not found!")

        else:

            print("Invalid choice!")

    # UPDATE STUDENT

    def update_student(self):

        student_id = input("Enter Student ID: ").strip()

        student = self.students.get(student_id)

        if not student:

            print("Student not found!")
            return

        print("\n1. Update Name")
        print("2. Update Age")
        print("3. Update Email")
        print("4. Update Department")
        print("5. Update Subject Marks")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter New Name: ").strip()

            if name and all(part.isalpha() for part in name.split()):

                student.name = name

            else:

                print("Invalid name!")
                return

        elif choice == "2":

            try:

                age = int(input("Enter New Age: "))

                if age <= 0 or age > 120:

                    print("Invalid age!")
                    return

                student.age = age

            except ValueError:

                print("Invalid age!")
                return

        elif choice == "3":

            email = input("Enter New Email: ").strip()

            if "@" not in email or "." not in email:

                print("Invalid email!")
                return

            student.email = email

        elif choice == "4":

            department = input("Enter New Department: ").strip()

            if not department:

                print("Department cannot be empty!")
                return

            student.department = department

        elif choice == "5":

            for subject in student.marks:

                try:

                    mark = float(input(f"Enter {subject} Marks: "))

                    if mark < 0 or mark > 100:

                        print("Marks must be between 0 and 100!")
                        return

                    student.marks[subject] = mark

                except ValueError:

                    print("Invalid marks!")
                    return

        else:

            print("Invalid choice!")
            return

        self.save_data()

        print("Student updated successfully!")

    # DELETE STUDENT
  
    def delete_student(self):

        student_id = input("Enter Student ID: ").strip()

        if student_id not in self.students:

            print("Student not found!")
            return

        confirm = input(
            "Are you sure you want to delete this student? (yes/no): "
        ).strip().lower()

        if confirm == "yes":

            del self.students[student_id]

            self.save_data()

            print("Student deleted successfully!")

        else:

            print("Deletion cancelled!")

# Academic Management 
    # Calculate total marks
    def calculate_total(self, student):
        return sum(student.marks.values())

    # Calculate average percentage
    def calculate_average(self, student):
        total = self.calculate_total(student)
        maximum_marks = len(student.marks) * 100

        if maximum_marks == 0:
            return 0

        return (total / maximum_marks) * 100

    # Assign grade
    def calculate_grade(self, percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "F"

    # Determine pass or fail
    def get_status(self, percentage):
        if percentage >= 60:
            return "Pass"
        else:
            return "Fail"

    # Generate individual student report
    def generate_report(self):
        student_id = input("Enter Student ID: ")

        student = self.students.get(student_id)

        if student is None:
            print("Student not found!")
            return

        total = self.calculate_total(student)
        percentage = self.calculate_average(student)
        grade = self.calculate_grade(percentage)
        status = self.get_status(percentage)

        print("\n STUDENT RESULT REPORT ")
        print("Student ID:", student.student_id)
        print("Name:", student.name)
        print("Department:", student.department)

        print("\nSubject Marks:")

        for subject, marks in student.marks.items():
            print(subject, ":", marks)

        print("\nTotal Marks:", total, "/", len(student.marks) * 100)
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)
        print("Status:", status)
        print("__________________________________")

    # Display passed students
    def display_passed_students(self):
        print("\n PASSED STUDENTS ")

        found = False

        for student in self.students.values():
            percentage = self.calculate_average(student)

            if self.get_status(percentage) == "Pass":
                print(
                    student.name,
                    "| Percentage:", round(percentage, 2), "%",
                    "| Grade:", self.calculate_grade(percentage)
                )
                found = True

        if not found:
            print("No students passed.")

    # Display failed students
    def display_failed_students(self):
        print("\n FAILED STUDENTS ")

        found = False

        for student in self.students.values():
            percentage = self.calculate_average(student)

            if self.get_status(percentage) == "Fail":
                print(
                    student.name,
                    "| Percentage:", round(percentage, 2), "%",
                    "| Grade:", self.calculate_grade(percentage)
                )
                found = True

        if not found:
            print("No students failed.")

    # Find highest-scoring student
    def display_highest_student(self):
        if not self.students:
            print("No students available.")
            return

        highest = max(
            self.students.values(),
            key=self.calculate_average
        )

        percentage = self.calculate_average(highest)

        print("\n HIGHEST-SCORING STUDENT ")
        print("Name:", highest.name)
        print("Student ID:", highest.student_id)
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", self.calculate_grade(percentage))

    # Find lowest-scoring student
    def display_lowest_student(self):
        if not self.students:
            print("No students available.")
            return

        lowest = min(
            self.students.values(),
            key=self.calculate_average
        )
        percentage = self.calculate_average(lowest)
        print("\n LOWEST-SCORING STUDENT ")
        print("Name:", lowest.name)
        print("Student ID:", lowest.student_id)
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", self.calculate_grade(percentage))

    def search_by_id(self):
        student_id = input("Enter Student ID: ")

        student = self.students.get(student_id)

        if student:
            student.display_student()
        else:
            print("Student not found!")

    def search_by_name(self):
        name = input("Enter Full Name: ").strip().lower()

        found = False

        for student in self.students.values():
            if student.name.lower() == name:
                student.display_student()
            found = True

            if not found:
                print("Student not found!")
    def filter_by_department(self):
            department = input("Enter Department: ").strip().lower()

            found = False

            for student in self.students.values():
                if student.department.lower() == department:
                    student.display_student()
            found = True

            if not found:
                print("No students found in this department.")
    def filter_by_grade(self):
            grade = input("Enter Grade (A+, A, B, C, F): ").strip().upper()

            found = False

            for student in self.students.values():
                percentage = self.calculate_average(student)
                student_grade = self.calculate_grade(percentage)

                if student_grade == grade:
                    student.display_student()
                found = True

                if not found:
                    print("No students found with this grade.")
    def sort_by_name(self):
            sorted_students = sorted(
            self.students.values(),
            key=lambda student: student.name.lower()
    )

            for student in sorted_students:
                student.display_student()
    def sort_by_average(self):
            sorted_students = sorted(
            self.students.values(),
            key=self.calculate_average,
            reverse=True
    )

            for student in sorted_students:
                percentage = self.calculate_average(student)

            print(
            student.name,
            "| Average:", round(percentage, 2), "%"
        )
    
    def display_top_three(self):
        top_students = sorted(
            self.students.values(),
            key=self.calculate_average,
            reverse=True
        )[:3]

        print("\n TOP 3 STUDENTS ")

        if not top_students:
            print("No students available.")
            return

        for rank, student in enumerate(top_students, start=1):
            percentage = self.calculate_average(student)

            print(
                rank,
                student.name,
                "| Average:", round(percentage, 2), "%"
            )
    def display_class_statistics(self):

        total_students = len(self.students)

        passed_students = 0
        failed_students = 0

        total_average = 0

        grade_count = {
            "A+": 0,
            "A": 0,
            "B": 0,
            "C": 0,
            "F": 0
        }

        department_count = {}

        if total_students == 0:
            print("No students registered yet.")
            return

        for student in self.students.values():

            percentage = self.calculate_average(student)
            grade = self.calculate_grade(percentage)
            status = self.get_status(percentage)

            total_average += percentage

            if status == "Pass":
                passed_students += 1
            else:
                failed_students += 1

            grade_count[grade] += 1

            department = student.department

            if department in department_count:
                department_count[department] += 1
            else:
                department_count[department] = 1
                class_average = total_average / total_students

        highest_student = max(
            self.students.values(),
            key=self.calculate_average
        )

        lowest_student = min(
            self.students.values(),
            key=self.calculate_average
        )

        highest_average = self.calculate_average(highest_student)
        lowest_average = self.calculate_average(lowest_student)

        print("\n CLASS STATISTICS ")

        print("Total Registered Students:", total_students)
        print("Total Passed Students:", passed_students)
        print("Total Failed Students:", failed_students)

        print("Overall Class Average:", round(class_average, 2), "%")

        print(
            "Highest Student:",
            highest_student.name,
            "| Average:", round(highest_average, 2), "%"
        )

        print(
            "Lowest Student:",
            lowest_student.name,
            "| Average:", round(lowest_average, 2), "%"
        )

        print("\n GRADE-WISE COUNT ")

        for grade, count in grade_count.items():
            print(grade, ":", count)

        print("\n DEPARTMENT-WISE COUNT ")

        for department, count in department_count.items():
            print(department, ":", count)
        print("\n__________________________________") 


# MAIN APPLICATION
def main():

    manager = StudentManager()

    while True:

        print("\n____________________________________")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("______________________________________")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("7. Generate Student Result Report")
        print("8. Display Passed Students")
        print("9. Display Failed Students")
        print("10. Display Highest-Scoring Student")
        print("11. Display Lowest-Scoring Student")
        print("12. Search Student by ID")
        print("13. Search Student by Name")
        print("14. Filter by Department")
        print("15. Filter by Grade")
        print("16. Sort Students by Name")
        print("17. Sort Students by Average")
        print("18. Display Top 3 Students") 
        print("19. Display Class Statistics")
        choice = input("\n Enter Your Choice: ")

        if choice == "1":

            manager.add_student()

        elif choice == "2":

            manager.display_students()

        elif choice == "3":

            manager.search_student()

        elif choice == "4":

            manager.update_student()

        elif choice == "5":

            manager.delete_student()

        elif choice == "6":

            print("Thank you for using Student Management System!")
            break

        elif choice == "7":
            manager.generate_report()

        elif choice == "8":
            manager.display_passed_students()

        elif choice == "9":
            manager.display_failed_students()

        elif choice == "10":
            manager.display_highest_student()

        elif choice == "11":
            manager.display_lowest_student()
        elif choice == "12":
            manager.search_by_id()

        elif choice == "13":
            manager.search_by_name()

        elif choice == "14":
            manager.filter_by_department()

        elif choice == "15":
            manager.filter_by_grade()

        elif choice == "16":
            manager.sort_by_name()

        elif choice == "17":
            manager.sort_by_average()
        elif choice == "18":
            manager.display_top_three()

        elif choice == "19":
            manager.display_class_statistics()
        else:
           print("Invalid choice! Please try again.")


if __name__ == "__main__":

    main()
