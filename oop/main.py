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
        
# Contoh inheritance
class greet(Person):
    def say_hello(self):
        return f"Hello, my name is {self.get_name()} and I am {self.get_age()} years old. I live at {self.get_address()}."

# createing objects
person1 = greet("John", 30, "New York")
print(person1.say_hello())

# Mini Challenge Class, Object, Encapsulation
# init -> constrcuctor method, digunakan untuk menginisialisasi atribut dari sebuah objek saat objek tersebut dibuat.
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

# Abstraction = untuk menyembunyikan detail implementasi dari pengguna dan hanya menampilkan fungsionalitas yang relevan. 
# Abstraction dapat dicapai melalui penggunaan abstract class dan abstract method.
class Fruit:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def describe(self):
        return f"This is a {self.get_color()} {self.get_name()}."

class Apple(Fruit):
    def __init__(self, name, color, taste):
        super().__init__(name, color) # ini dari class Fruit
        self.__taste = taste

    def get_taste(self):
        return self.__taste

    def describe(self):
        return f"This is a {self.get_color()} {self.get_name()} and it tastes {self.get_taste()}."
    
    
apple1 = Apple("Apple", "Red", "Sweet")
print(apple1.describe())
    
# Mini Challenge Abstraction
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    @abstractmethod
    def describe(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors

    def get_num_doors(self):
        return self.__num_doors

    def describe(self):
        return f"This is a {self.get_make()} {self.get_model()} with {self.get_num_doors()} doors."

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.__has_sidecar = has_sidecar
        
    def get_has_sidecar(self):
        return self.__has_sidecar

    def describe(self):
        sidecar_status = "with a sidecar" if self.get_has_sidecar() else "without a sidecar"
        return f"This is a {self.get_make()} {self.get_model()} {sidecar_status}."

car1 = Car("Toyota", "Camry", 4)
print(car1.describe())

motorcycle1 = Motorcycle("Harley-Davidson", "Street 750", False)
print(motorcycle1.describe())

# Mini Challenge Polymorphism
class Vehicle:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model
    
    def move(self):
        return self._move()

    def move_forward(self):
        return f"{self.get_make()} {self.get_model()} is moving forward."

    def move_backward(self):
        return f"{self.get_make()} {self.get_model()} is moving backward."

    def change_gear(self, gear):
        return f"{self.get_make()} {self.get_model()} changed to gear {gear}."
    
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors

    def get_num_doors(self):
        return self.__num_doors
    
    def move(self):
        return f"{self.get_make()} {self.get_model()} is moving"
    
class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.__has_sidecar = has_sidecar

    def get_has_sidecar(self):
        return self.__has_sidecar
    
    # ini contoh polymorphism, method move() di override
    def move(self):
            return f"{self.get_make()} {self.get_model()} is riding"

car1 = Car("Honda", "Civic", 4)
print(car1.change_gear(2))
print(car1.move_forward())  
print(car1.move())

motorcycle1 = Motorcycle("Yamaha", "MT-07", False)
print(motorcycle1.move_backward())
print(motorcycle1.move())

# Internal modules
import shape
print(shape.volume_kubus(4))
print(shape.volume_balok(2, 3, 4))
print(shape.volume_tabung(5, 10))