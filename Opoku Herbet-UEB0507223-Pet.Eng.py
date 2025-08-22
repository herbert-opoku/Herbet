# ASSIGNMENT 1
# Task 1
herbet = 985
opoku = 34.89
john = 'train'
kwame = True
print(herbet, type(herbet))
print(opoku, type(opoku))
print(john, type(john))
print(kwame, type(kwame))

# Task 2
int(19.99), type(int(19.99))
str(50), type(str(50))
float('50'), type('50')
float('50'), type(float('50'))

# Task 3
first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
print('Hello '+first_name, last_name+'!')

# Task 4
age = 20
print("You are " + str(age) +" years old ")

 # Task 5
fav_word = input('Enter your favourite word:')
repeat = input('How many times should it be repeated:')
print((fav_word+" ")*int(repeat))

# Task 6
a : SyntaxError
b : ValueError
c : TypeError

# ASSIGNMENT 2 
# Task 1
rex = 'Hello'
slim = 'here'
rake = 'LOVELY'
print(rex.lower())

print(slim.lower())

print(rake.lower())

# Task 2(all upper case turns lower case and all lower case turns upper case)
fame = 'HeLLo WoRLd'
print(fame.swapcase())

# Task 3 (remmove all upper case leters)

def remove_uppercase(s: str) -> str:
    return ''.join(ch for ch in s if not ch.isupper())

# Example usage
print(remove_uppercase("HelloWorld"))

#Task 4(return the number of uppercase and lowercase letters in that string)
n = 'EngiNEEr'

uppercase = 0
lowercase = 0

for letter in n:
    if letter.isupper():
        uppercase += 1
    elif letter.islower():
        lowercase += 1

print(f'The number of uppercase is {uppercase} and lowercase is {lowercase}')

# TASK 5
import re

word = "Data-Driven@2025!"
output6 = re.sub(r'[^a-zA-Z]', '', word)
print(output6)

# TASK6
import math

a = 3
b = 4
c = 5
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f'The area is {area}')

# TASK7
names = ["mbuemo", "cuhna", "sesko", "eze", "gyokeres"]
max_len = max(len(names) for name in names)

print("name".ljust(max_len + 2) + "length".rjust(6))
print("-" * (max_len + 2))
for name in names:
    print(name.ljust(max_len + 2) + str(len(name)).rjust(6))
    
    #Task 8
    import string

def clean_string(s: str) -> str:
    # Remove leading/trailing whitespace
    s = s.strip()
    
    # Replace punctuation with empty string
    s = s.translate(str.maketrans('', '', string.punctuation))
    
    # Remove all spaces
    s = s.replace(" ", "")
    
    return s

# Example usage
input_str = " Hello, World! "
output_str = clean_string(input_str)
print(output_str)  # Output: "HelloWorld"

# ASSINGMENT 3
#randomly guess a number
import random
print("you have 20 chances")
user = int(input("enter a number between 1,200: "))
guess = random.randint(1, 200)
for i in range(20):
  if user == guess:
    print("you guessed right")
    break
  elif user > guess:
    print("your guess is higher")
    user = int(input("try again enter another number: "))
    continue
  elif user < guess:
    print("your guess is lower")
    user = int(input("try again enter another number: "))
    continue
  else:
    print("your number is not realistic")
else:
  print("you runned out of chances")
  
  

# ASSIGNMENT 4(USING TRY AND EXCEPT IN ASSSIGNMENT 1 AND 2)
# Task 1
herbet = 985
opoku = 34.89
john = 'train'
kwame = True
print(herbet, type(herbet))
print(opoku, type(opoku))
print(john, type(john))
print(kwame, type(kwame))

# Task 2
# a. Float → Integer
num_float = 19.99
num_int = int(num_float)
print(num_int, type(num_int))

# b. Integer → String
num_integer = 50
num_str = str(num_integer)
print(num_str, type(num_str))

# c. String → Float
str_num = "50"
num_float2 = float(str_num)
print(num_float2, type(num_float2))


# Task 3
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, " + first_name + " " + last_name + "!")


# Task 4
age = 20

# Fixed version (convert int to str before concatenation)
print("You are " + str(age) + " years old.")

# Task 5
word = input("Enter your favourite word: ")
count = int(input("How many times to repeat it? "))

# Repeat with spaces
print((word + " ") * count)
# Task 6
try:
    eval('print("Hello')   # SyntaxError
except SyntaxError:
    print("Caught a SyntaxError")

try:
    int("abc")            # ValueError
except ValueError:
    print("Caught a ValueError")

try:
    result = "age" + 10   # TypeError
except TypeError:
    print("Caught a TypeError")

try:
    print('unknown_var')    # NameError
except NameError:
    print("Caught a NameError")
    
    
    #FOR ASSIGNMENT 2
    # Task 1
try:
    s = "Hello"
    result = s.lower()
    print("Task 1 Output:", result)
except Exception as e:
    print("Error in Task 1:", e)


# Task 2
try:
    s = "HeLLo WoRLd"
    result = s.swapcase()
    print("Task 2 Output:", result)
except Exception as e:
    print("Error in Task 2:", e)


# Task 3
try:
    s = "HelloWorld"
    result = "".join([ch for ch in s if not ch.isupper()])
    print("Task 3 Output:", result)
except Exception as e:
    print("Error in Task 3:", e)

# Task 4
try:
    s = "EngiNEEr"
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    print(f"Task 4 Output: Uppercase: {upper}, Lowercase: {lower}")
except Exception as e:
    print("Error in Task 4:", e)


# Task 5
import string

try:
    s = "Data-Driven@2025!"
    result = "".join([ch for ch in s if ch.isalpha()])
    print("Task 5 Output:", result)
except Exception as e:
    print("Error in Task 5:", e)


# Task 6
import math

try:
    a, b, c = 3, 4, 5
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Task 6 Output:", area)
except Exception as e:
    print("Error in Task 6:", e)


# Task 7
try:
    names = ["Alice", "Bob", "Catherine", "David"]
    print("Task 7 Output:\n")
    print("Name".ljust(15, " "))
    print("-" * 15)
    for name in names:
        print(name.ljust(15, " "))
except Exception as e:
    print("Error in Task 7:", e)
    
    
    # Task 8
try:
    import string
    s = " Hello, World! "

    # i. Strip leading/trailing spaces
    cleaned = s.strip()

    # ii. Remove punctuation
    cleaned = "".join(ch for ch in cleaned if ch not in string.punctuation)

    # iii. Remove all spaces
    cleaned = cleaned.replace(" ", "")

    print("Task 8 Output:", cleaned)
except Exception as e:
    print("Error in Task 8:", e)
    
    
    #ASSIGNMENT 5(USING FUNCTIONS FOR ASSIGNMENT 1 AND 2)
# Task 1
def task1():
    print("\n--- Task 1 ---")
    integer_var = 10
    float_var = 19.5
    string_var = "Hello"
    boolean_var = True
    
    print(integer_var, type(integer_var))
    print(float_var, type(float_var))
    print(string_var, type(string_var))
    print(boolean_var, type(boolean_var))


# Task 2
def task2():
    print("\n--- Task 2 ---")
    # a. Float → Integer
    num_float = 19.99
    num_int = int(num_float)
    print(num_int, type(num_int))

    # b. Integer → String
    num_integer = 50
    num_str = str(num_integer)
    print(num_str, type(num_str))

    # c. String → Float
    str_num = "50"
    num_float2 = float(str_num)
    print(num_float2, type(num_float2))


# Task 3
def task3():
    print("\n--- Task 3 ---")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("Hello, " + first_name + " " + last_name + "!")


# Task 4
def task4():
    print("\n--- Task 4 ---")
    age = 20
    # Corrected version
    print("You are " + str(age) + " years old.")
    print("Explanation: Cannot concatenate 'str' with 'int' without converting the int to string.")


# Task 5
def task5():
    print("\n--- Task 5 ---")
    word = input("Enter your favourite word: ")
    count = int(input("How many times to repeat it? "))
    print((word + " ") * count)


# Task 6
def task6():
    print("\n--- Task 6 ---")

    # Matching error codes with types inside functions
    def syntax_error_demo():
        try:
            eval('print("Hello')   # incomplete string literal = SyntaxError
        except SyntaxError:
            print("Caught a SyntaxError")

    def value_error_demo():
        try:
            int("abc")          # Cannot convert "abc" to int
        except ValueError:
            print("Caught a ValueError")

    def type_error_demo():
        try:
            result = "age" + 10  # Cannot add str + int
        except TypeError:
            print("Caught a TypeError")

    def name_error_demo():
        try:
            print('not_defined_var')  # Variable not defined
        except NameError:
            print("Caught a NameError")

    # Run all
    syntax_error_demo()
    value_error_demo()
    type_error_demo()
    name_error_demo()

# Main function to run everything
def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()


# Run program
if name == "_main_":
    main()
    
    #FOR ASSIGNMENT 2
    import math
import string

# Task 1: Convert all uppercase to lowercase
def task1(s):
    return s.lower()

# Task 2: Swap uppercase <-> lowercase
def task2(s):
    return s.swapcase()

# Task 3: Remove uppercase letters
def task3(s):
    return "".join([ch for ch in s if not ch.isupper()])
                   
# Task 4: Count uppercase and lowercase
def task4(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return f"Uppercase: {upper}, Lowercase: {lower}"

# Task 5: Remove non-English letters
def task5(s):
    return "".join([ch for ch in s if ch.isalpha()])

# Task 6: Heron’s Formula for triangle area
def task6(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Task 7: Format names neatly in a table
def task7(names):
    output = "Name".ljust(15) + "\n" + "-"*15 + "\n"
    for name in names:
        output += name.ljust(15) + "\n"
    return output

# Task 8: Clean string → strip, remove punctuations, remove spaces
def task8(s):
    s = s.strip()
    s = "".join(ch for ch in s if ch not in string.punctuation)
    s = s.replace(" ", "")
    return s


    
    #ASSIGNMENT 6(Select at least six formulas in your field. Implement them using classes, objects and methods. Also apply OOP concepts such as polymorphism and inheritance. Use try/catch to handle potential errors.)
    import math
class Formula:
    """Base class for all formulas"""
    def calculate(self):
        raise NotImplementedError("This method should be overridden in subclasses")


# 1. Pressure = Force / Area
class Pressure(Formula):
    def __init__(self, force, area):
        self.force = force
        self.area = area

    def calculate(self):
        try:
            return self.force / self.area
        except ZeroDivisionError:
            return "Error: Area cannot be zero"


# 2. Density = Mass / Volume
class Density(Formula):
    def __init__(self, mass, volume):
        self.mass = mass
        self.volume = volume

    def calculate(self):
        try:
            return self.mass / self.volume
        except ZeroDivisionError:
            return "Error: Volume cannot be zero"


# 3. Work = Force * Distance
class Work(Formula):
    def __init__(self, force, distance):
        self.force = force
        self.distance = distance

    def calculate(self):
        return self.force * self.distance


# 4. Kinetic Energy = 1/2 * m * v^2
class KineticEnergy(Formula):
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

    def calculate(self):
        return 0.5 * self.mass * (self.velocity ** 2)


# 5. Ideal Gas Law: PV = nRT
class IdealGasLaw(Formula):
    R = 8.314  # Universal gas constant J/(mol*K)

    def __init__(self, n, T, V):
        self.n = n
        self.T = T
        self.V = V

    def calculate(self):
        try:
            return (self.n * IdealGasLaw.R * self.T) / self.V
        except ZeroDivisionError:
            return "Error: Volume cannot be zero"


# 6. Efficiency = W_out / Q_in
class Efficiency(Formula):
    def __init__(self, W_out, Q_in):
        self.W_out = W_out
        self.Q_in = Q_in

    def calculate(self):
        try:
            return self.W_out / self.Q_in
        except ZeroDivisionError:
            return "Error: Heat input cannot be zero"


# Demonstrating Polymorphism (all subclasses share 'calculate')
formulas = [
    Pressure(100, 5),
    Density(50, 10),       # Will trigger error
    Work(200, 10),
    KineticEnergy(60, 15),
    IdealGasLaw(2, 300, 6),  # Will trigger error
    Efficiency(500, 1000)
]

for f in formulas:
    print(f"{f.__class__.__name__}: {f.calculate()}")


