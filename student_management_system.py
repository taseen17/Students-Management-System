class Student():
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    @property
    def student_id(self):
        return self.__student_id
    @property
    def name(self):
        return self.__name  
    @property
    def department(self):
        return self.__department
    @property
    def is_enrolled(self):
        return self.__is_enrolled
    @is_enrolled.setter
    def is_enrolled(self, value):
        self.__is_enrolled = value

    def enroll_student(self, student):
        for s in self.student_list:
            if s.student_id == student.student_id and student.is_enrolled == False:
                student.is_enrolled = True
                return f"Student {student.name} has been enrolled."
            elif s.student_id == student.student_id and student.is_enrolled == True:
                return f"Student {student.name} is already enrolled."

    def drop_student(self, student):
        for s in self.student_list:
            if s.student_id == student.student_id and student.is_enrolled == True:
                student.is_enrolled = False
                return f"Student {student.name} has been dropped."
            elif s.student_id == student.student_id and student.is_enrolled == False:
                return f"Student {student.name} is not enrolled."

    def view_student_info(self, student):
        for s in self.student_list:
            if s.student_id == student.student_id:
                print(f"Student ID: {s.student_id}, Name: {s.name}, Department: {s.department}, Enrolled: {s.is_enrolled}")

class StudentDatabase(Student):
    student_list = []

    def __init__(self):
        super().__init__(student_id=None, name=None, department=None, is_enrolled=False)

    def add_student(self, student):
        self.student_list.append(student) 

sadiqah = Student(1, "Sadiqah", "Computer Science", False)
shamha = Student(2, "Shamha", "Mathematics", False)
student_db = StudentDatabase()
student_db.add_student(sadiqah)
student_db.add_student(shamha)

while True:
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        for student in student_db.student_list:
            student_db.view_student_info(student)
    elif choice == '2':
        student_id = int(input("Enter student ID to enroll: "))
        for student in student_db.student_list:
            if student.student_id == student_id:
                result = student_db.enroll_student(student)
                print(result)
                break
        else:
            print("Student not found.")
    elif choice == '3':
        student_id = int(input("Enter student ID to drop: "))
        for student in student_db.student_list:
            if student.student_id == student_id:
                result = student_db.drop_student(student)
                print(result)
                break
        else:
            print("Student not found.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:        
        print("Invalid choice. Please try again.")