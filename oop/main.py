# Python OOP & Modular Programming

# Class, Object, Encapsulation, Inheritance
class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    # access modifier = untuk mengatur akses ke atribut dan method dalam sebuah class. Ada 3 jenis access modifier di Python:
    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_address(self, address):
        self.__address = address
        
class greet(Person):
    def say_hello(self):
        return f"Hello, my name is {self.get_name()} and I am {self.get_age()} years old. I live at {self.get_address()}."

# createing objects
person1 = greet("John", 30, "New York")
print(person1.say_hello())

# Mini Challenge Class, Object, Encapsulation
class Animal:
    def __init__(self, name, species, total_legs):
        self.__name = name
        self.__species = species
        self.__total_legs = total_legs

    # Getter methods
    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_total_legs(self):
        return self.__total_legs

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_species(self, species):
        self.__species = species

    def set_total_legs(self, total_legs):
        self.__total_legs = total_legs
        
class cat(Animal):
    pass

cat1 = cat("Whiskers", "Feline", 4)
print(f"My cat's name is {cat1.get_name()}, it is a {cat1.get_species()} and it has {cat1.get_total_legs()} legs.")
