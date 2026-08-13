# Python Fundamentals

print("Hello, World!")

age = 25
print("Hello, I am", age, "years old.")

# Object
person = {
    "name": "John",
    "age": 30,
    "address": "New York"
}
print("Hello, my name is", person["name"], "and I am", person["age"], "years old. I live at", person["address"] + ".")


# Basic Operators
numberOne = 5
numberTwo = 3
print("The sum of", numberOne, "and", numberTwo, "is", numberOne + numberTwo)
print("The difference between", numberOne, "and", numberTwo, "is", numberOne - numberTwo)
print("The product of", numberOne, "and", numberTwo, "is", numberOne * numberTwo)
print("The quotient of", numberOne, "and", numberTwo, "is", numberOne / numberTwo)
print("The remainder of", numberOne, "divided by", numberTwo, "is", numberOne % numberTwo)

# If Condition
score = 85
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
else:
    print("You did not get an A.")
    
# Switch Condition
match score:
    case score if score >= 90:
        print("You got an A!")
    case score if score >= 80:
        print("You got a B!")
    case _:
        print("You got a C or below.")
        
# Mini Challenge
totalWin =5
if totalWin > 5:
    print("World Champion #5")
elif totalWin < 5:
    print("World Champion #0")
else:
    print("Bukan World Champions")
    
# Looping
# For
for i in range(5):
    print("This is iteration number", i + 1)

# While
i = 0
while i < 5:
    print("This is iteration number", i + 1)
    i += 1
    
# For Each
nations = ["USA", "Canada", "Mexico", "Brazil", "Argentina"]
for nation in nations:
    print("I have visited", nation, ".")
    
# Mini Challenge FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Functions
def showMessage(message):
    print(message)

showMessage("Hello, this is a message from a function!")

def multiplication(num1, num2):
    return num1 * num2

result = multiplication(5, 3)
print("The result of multiplication is", result)

# Mini Challenge Functions
def OddorEven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
for i in range(1, 101):
    print(i, "is", OddorEven(i))
    
# Error Handling
result = 10 / 0

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
# Mini Challenge Error Handling
def divideByFifty(num):
    try:
        result = num / 50
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"An error occurred: {e}"