


# diferent dynamic classes

class Student:
    def __init__(self, name, age, gender, student_id, course, year, gpa):
        self.name = name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

class Teacher:
    def __init__(self, name, subject, emp_id, age, gender, experience, salary):
        self.name = name
        self.subject = subject
        self.emp_id = emp_id
        self.age = age
        self.gender = gender
        self.experience = experience
        self.salary = salary

class Course:
    def __init__(self, course_id, title, credits, duration, level, department, lecturer):
        self.course_id = course_id
        self.title = title
        self.credits = credits
        self.duration = duration
        self.level = level
        self.department = department
        self.lecturer = lecturer

class Book:
    def __init__(self, isbn, title, author, publisher, year, genre, pages):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.pages = pages

class Car:
    def __init__(self, brand, model, year, color, engine, fuel_type, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.fuel_type = fuel_type
        self.price = price

class Employee:
    def __init__(self, emp_id, name, department, position, salary, age, gender):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary
        self.age = age
        self.gender = gender

class Hospital:
    def __init__(self, name, location, capacity, departments, doctors, nurses, patients):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.departments = departments
        self.doctors = doctors
        self.nurses = nurses
        self.patients = patients



# Creating 7 objects for each class

# Students
students = [
    Student("Alice", 20, "Female", "S001", "CS", 2, 3.6),
    Student("Bob", 22, "Male", "S002", "IT", 3, 3.2),
    Student("Carol", 21, "Female", "S003", "SE", 2, 3.8),
    Student("David", 23, "Male", "S004", "DS", 4, 3.1),
    Student("Eve", 20, "Female", "S005", "AI", 2, 3.7),
    Student("Frank", 24, "Male", "S006", "Math", 4, 3.4),
    Student("Grace", 22, "Female", "S007", "CS", 3, 3.9),
]

# Teachers
teachers = [
    Teacher("Mr. John", "Math", "T001", 40, "Male", 12, 1200),
    Teacher("Ms. Rose", "CS", "T002", 35, "Female", 10, 1500),
    Teacher("Dr. Smith", "AI", "T003", 50, "Male", 20, 2000),
    Teacher("Mrs. Jane", "SE", "T004", 38, "Female", 11, 1300),
    Teacher("Mr. Mike", "IT", "T005", 45, "Male", 15, 1600),
    Teacher("Dr. Lucy", "DS", "T006", 42, "Female", 14, 1700),
    Teacher("Mr. Dan", "Math", "T007", 37, "Male", 9, 1100),
]

# Courses
courses = [
    Course("C001", "Intro to CS", 3, "3 months", "Beginner", "CS Dept", "Dr. Smith"),
    Course("C002", "AI Basics", 4, "4 months", "Intermediate", "AI Dept", "Dr. Lucy"),
    Course("C003", "Data Science", 5, "6 months", "Advanced", "DS Dept", "Dr. Mike"),
    Course("C004", "Software Eng", 4, "4 months", "Intermediate", "SE Dept", "Mrs. Jane"),
    Course("C005", "Networks", 3, "3 months", "Beginner", "IT Dept", "Mr. Dan"),
    Course("C006", "Machine Learning", 5, "5 months", "Advanced", "AI Dept", "Dr. Smith"),
    Course("C007", "Math for CS", 3, "3 months", "Beginner", "Math Dept", "Mr. John"),
]

# Books
books = [
    Book("B001", "Python 101", "John Doe", "Pearson", 2019, "Programming", 300),
    Book("B002", "AI for All", "Jane Smith", "O'Reilly", 2020, "AI", 350),
    Book("B003", "Data Science Handbook", "Mike Ross", "Springer", 2018, "DS", 400),
    Book("B004", "Machine Learning", "Tom Lee", "MIT Press", 2021, "ML", 450),
    Book("B005", "Algorithms", "CLRS", "MIT", 2009, "CS", 1200),
    Book("B006", "Database Systems", "Navathe", "Pearson", 2015, "DBMS", 600),
    Book("B007", "Computer Networks", "Tanenbaum", "Pearson", 2017, "Networking", 700),
]

# Cars
cars = [
    Car("Toyota", "Corolla", 2020, "White", "1.8L", "Petrol", 20000),
    Car("Honda", "Civic", 2019, "Black", "2.0L", "Petrol", 22000),
    Car("Tesla", "Model 3", 2021, "Red", "Electric", "Electric", 35000),
    Car("Ford", "Mustang", 2018, "Blue", "5.0L", "Petrol", 40000),
    Car("BMW", "X5", 2020, "Gray", "3.0L", "Diesel", 50000),
    Car("Mercedes", "C300", 2021, "Silver", "2.0L", "Petrol", 45000),
    Car("Audi", "A4", 2019, "Black", "2.0L", "Petrol", 38000),
]

# Employees
employees = [
    Employee("E001", "John", "HR", "Manager", 3000, 35, "Male"),
    Employee("E002", "Lucy", "IT", "Developer", 2500, 29, "Female"),
    Employee("E003", "Mike", "Finance", "Analyst", 2800, 33, "Male"),
    Employee("E004", "Jane", "Sales", "Executive", 2600, 27, "Female"),
    Employee("E005", "Robert", "Admin", "Clerk", 2200, 31, "Male"),
    Employee("E006", "Sophia", "Marketing", "Lead", 3100, 30, "Female"),
    Employee("E007", "Daniel", "Operations", "Supervisor", 2700, 34, "Male"),
]

# Hospitals
hospitals = [
    Hospital("City Hospital", "NY", 200, 10, 50, 100, 500),
    Hospital("Green Valley", "LA", 300, 12, 70, 150, 700),
    Hospital("Sunrise Health", "Chicago", 250, 11, 60, 120, 600),
    Hospital("MediCare", "Boston", 180, 9, 40, 90, 400),
    Hospital("LifeCare", "Houston", 350, 15, 80, 200, 800),
    Hospital("Wellness Center", "Miami", 220, 10, 55, 110, 550),
    Hospital("HealthFirst", "Dallas", 270, 12, 65, 130, 650),
]
