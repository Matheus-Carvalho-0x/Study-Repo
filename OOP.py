"""
Advantages of OOP:
Provides a clear structure to programs
Makes code easier to maintain, reuse, and debug
Helps keep your code DRY (Don't Repeat Yourself)
Allows you to build reusable applications with less code
"""
# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:
# When you modify a class property, it affects all objects.


class Person:
    species = "Human"  # Class property

    def __init__(self, name):
        self.name = name  # Instance property


p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# Note: All methods must have self as the first parameter.
# The __str__() Method
# The __str__() method is a special method that controls what is returned when the object is printed


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)

"""
Why Use Encapsulation?
Encapsulation provides several benefits:

Data Protection: Prevents accidental modification of data
Validation: You can validate data before setting it
Flexibility: Internal implementation can change without affecting external code
Control: You have full control over how data is accessed and modified
"""
# Note: Private properties (.__) cannot be accessed directly from outside the class.
# Note: A single underscore _ is just a convention. It tells other programmers that the
# property is intended for internal use, but Python doesn't enforce this restriction.
# Note: Just like private properties with double underscores, private methods cannot be
# called directly from outside the class. The __validate method can only be used by other methods inside the class.
"""
Name Mangling
Name mangling is how Python implements private properties and methods.
When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.
For example, __age becomes _Person__age.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age)  # Not recommended!
# Note: While you can access private properties using the mangled name, it's not recommended. It defeats the purpose of encapsulation.

"""
Python Inner Classes
An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.
Inner classes are useful for grouping classes that are only used in one place, making your code more organized.
"""
# To access the inner class, create an object of the outer class, and then create an object of the inner class:


class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("Hello from inner class")


outer = Outer()
inner = outer.Inner()
inner.display()

"""
Accessing Outer Class from Inner Class
Inner classes in Python do not automatically have access to the outer class instance.
If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:
"""


class Outer:
    def __init__(self):
        self.name = "Emil"

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print(f"Outer class name: {self.outer.name}")


outer = Outer()
inner = outer.Inner(outer)
inner.display()


# Practical Example
# Inner classes are useful for creating helper classes that are only used within the context of the outer class:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")


car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()


# A class can have multiple inner classes:
class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print("Processing data...")

    class RAM:
        def store(self):
            print("Storing data...")


computer = Computer()
computer.cpu.process()
computer.ram.store()
