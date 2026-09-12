class Student:
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def display(self):
        print("Student ID :", self.student_id)
        print("Student Name:", self.name)
        print("Course      :", self.course)
        print("Year Level  :", self.year_level)


class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.array = [None] * self.capacity

    def add(self, student):
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = student
        self.size += 1

    def resize(self):
        new_capacity = self.capacity * 2

        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

        print("\nArray is full.")
        print("Increasing capacity...")

    def get(self, index):
        if index < 0 or index >= self.size:
            return None

        return self.array[index]

    def set(self, index, student):
        if index < 0 or index >= self.size:
            return False

        self.array[index] = student
        return True

    def search(self, student_id):
        for i in range(self.size):
            if self.array[i].student_id == student_id:
                return i

        return -1

    def remove(self, index):
        if index < 0 or index >= self.size:
            return False

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None

        self.size -= 1

        return True

    def display(self):
        if self.size == 0:
            print("\nNo student records found.")
            return

        print("\n========== STUDENT RECORDS ==========")

        for i in range(self.size):
            print("\nStudent", i + 1)
            print("-------------------------------------")
            self.array[i].display()

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity


def add_student(students):
    print("\n========== ADD STUDENT ==========")

    student_id = input("Enter Student ID: ")
    
    if students.search(student_id) != -1:
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    while True:
        try: 
            year_level = int(input("Enter Year Level: "))

            if year_level > 0:
                break
            else:
                print("Year Level must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    student = Student(student_id, name, course, year_level)

    students.add(student)

    print("\nStudent added successfully.")


def search_student(students):
    print("\n========== SEARCH STUDENT ==========")

    student_id = input("Enter Student ID: ")

    index = students.search(student_id)

    if index == -1:
        print("Student not found.")
    else:
        print("\nStudent found!")
        print("-------------------------------------")
        students.get(index).display()


def update_student(students):
    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID: ")

    index = students.search(student_id)

    if index == -1:
        print("Student not found.")
        return

    student = students.get(index)

    print("\nCurrent Information:")
    print("-------------------------------------")
    student.display()

    print("\nEnter New Information")

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    while True:
        try:
            year_level = int(input("Enter Year Level: "))

            if year_level > 0:
                break
            else:
                print("Year Level must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    updated_student = Student(
        student_id,
        name,
        course,
        year_level
    )

    students.set(index, updated_student)

    print("\nStudent updated successfully.")


def remove_student(students):
    print("\n========== REMOVE STUDENT ==========")

    student_id = input("Enter Student ID: ")

    index = students.search(student_id)

    if index == -1:
        print("Student not found.")
        return

    print("\nStudent to be removed:")
    print("-------------------------------------")
    students.get(index).display()

    #change Y/N to 1/2
    confirm = input("\nAre you sure you want to remove this student?"
                    "\n1. Yes"
                    "\n2. No\n")

    if confirm == "1":
            students.remove(index)
            print("\nStudent removed successfully.")
    else:
         print("\nRemove operation cancelled.")


def display_array_information(students):
    print("\n========== ARRAY INFORMATION ==========")
    print("Current Number of Students:", students.get_size())
    print("Current Array Capacity    :", students.get_capacity())
    print("Available Spaces          :",
          students.get_capacity() - students.get_size())


def main():
    students = DynamicArray()

    while True:
        print("\n")
        print("==============================================")
        print("          STUDENT RECORD MANAGER")
        print("==============================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            students.display()

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            remove_student(students)

        elif choice == "6":
            display_array_information(students)

        elif choice == "7":
            print("\nExiting Student Record Manager...")
            print("Thank you!")
            break

        else:
            print("\nInvalid choice. Please select 1-7.")

main()
