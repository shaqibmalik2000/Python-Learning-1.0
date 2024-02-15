# Initial learning of object oriented programming. Author: Shaqib Malik

# Object and Classes.

class Dog:

    def _init_(self, name, age):
        self.name = name    # Attribute created of class Dog called name.
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

d = Dog("Tim", 34)
d.set_age(23)
print(d.get_age())

# Part 2 - Multiple classes

class Student: 
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade
    
class Course:
    def _init_(self, name, max_students):
        self.name= name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s2 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())

# Part 3 - Inheritance

class Pet:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

class Cat(Pet): # Pet is inherited.
    def _init_(self, name, age, color):
        super()._init_(name, age)   # super calls to the super class that is inherited which is Pet. 
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "Brown")
c.show()
d = Dog("Jill", 25)
d.speak()

# Part 4 - Class attributes.

class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def _init_(self, name):
        self.name = name
        Person.number_of_people =+ 1

    @classmethod
    def number_of_people(cls):
        return cls.number_of_people()
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people_())

# Part 5 - Static methods

class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("run")
    
Math.pr()