#Getter and setter methods

class Student:
    def __init__(self, grade, name, age):
        self.__name = name
        self.__grade = grade
        self.age = age
        
        
    def set_grade(self):
        self.__grade = grade
    
    def get_grade(self):
        return self.__grade
        
    def set_name(self):
        self.__name = name
        
    def get_name(self):
        return self.__name
        
    def display(self):
        return self.__grade, self.__name, self.age
    


# Create a Student object with user input
name = input("Enter the name of the student: ")
grade = int(input("Enter the grade of the student: "))
age = int(input("Enter the age of the student: "))
student = Student(name, grade, age)

# Display initial information
print(student.display())

# Update the name and grade using setter methods
student.set_name("John Doe")
student.set_grade(12)

# Display updated information using getter methods and display method
print(f"Updated Name: {student.get_name()}")
print(f"Updated Grade: {student.get_grade()}")
print(student.display())