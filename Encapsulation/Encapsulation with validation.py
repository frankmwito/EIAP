# Encapsulation with validation

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute for age

    # Getter method for age with @property decorator
    @property
    def age(self):
        return self.__age

    # Setter method for age with validation
    @age.setter
    def age(self, value):
        if value not in range(0, 121):
            raise ValueError("Age must be between 0 and 120")
        else:
            self.__age = value

    # Method to display person details
    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")


# Example usage
try:
    person = Person("John", 25)

    # Accessing age using the getter
    print(f"Initial Age: {person.age}")
    
    # Setting a valid age using the setter
    person.age = 30
    print(f"Updated Age: {person.age}")
    
    # Attempting to set an invalid age
    person.age = 130  # This will raise a ValueError
except ValueError as e:
    print(e)

# Displaying person information
person.display()

            
