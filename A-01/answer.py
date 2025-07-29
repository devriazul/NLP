# Python Assignment - 01
# Topics: Python Fundamentals—Variables, Data Types, type conversion, and Input/Output


# 1. What happens if you assign a string value to a variable that previously held an integer?
# The variable will now hold the new string value instead of the integer.
# In Python, variables are dynamically typed, so the data type changes to match the new value.

# Example:
x = 10  # Now x is an integer
x = "Hello"  # Now x is a string


# 2. How can you check the data type of a variable in Python?
# Ans: By using the built-in type() function.

# Example:
x = 5
print(type(x))  # <class 'int'>

y = "hello"
print(type(y))  # <class 'str'>


# 3. What’s the difference between int("15") and str(15)?
# Ans:
# int("15") converts the string "15" to the integer 15.
# str(15) converts the integer 15 to the string "15".

# Example:
a = int("15")
print(a, type(a))  # 15 <class 'int'>

b = str(15)
print(b, type(b))  # "15" <class 'str'>


# 4. Write a Python program that takes two numbers as input from the user and performs arithmetic operations.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Exponentiation:", num1 ** num2)


# 5. How can you take multiple inputs from the user in a single line?
# Ans: By using input().split() method.

# Example:
a, b = input("Enter two numbers separated by space: ").split()
print("First number:", a)
print("Second number:", b)


# 6. What happens if you try to convert a string like "hello" to an integer using int()?
# Ans: Python will raise a ValueError because "hello" is not a valid integer.

# Example:
try:
    num = int("hello")
except ValueError as e:
    print("Error:", e)


# 7. Can a variable change its data type during program execution in Python?
# Ans: Yes! Python variables can change data types dynamically.

# Example:
v = 100  # integer
print(v, type(v))

v = "Python"  # string
print(v, type(v))


# 8. What’s the difference between the print() and input() functions?
# Ans:
# print() displays output on the screen.
# input() takes input from the user as a string.


# 9. Why does input() always return a string, and how do you handle it?
# Ans: To keep user input flexible, input() always returns a string.
# If you need another type, you must convert it manually.

# Example:
age = input("Enter your age: ")
age = int(age)
print("Your age plus 10 is:", age + 10)


# 10. How would you convert the string "15.5" to an integer, float, boolean & complex?

s = "15.5"
print("To float:", float(s))           # 15.5
print("To int:", int(float(s)))        # 15
print("To boolean:", bool(s))          # True (non-empty string is always True)
print("To complex:", complex(s))       # (15.5+0j)


# Bonus Questions

# 1. How does a variable work in memory? In Python, does it hold a reference or a value?
# Ans: In Python, a variable holds a reference to an object in memory, not the actual value directly.


# 2. What is the difference between mutable and immutable data types? Explain with real-life examples.
# Ans:
# Mutable: can be changed after creation (e.g., list, dict).
# Immutable: cannot be changed after creation (e.g., str, int, tuple).

# Example:
my_list = [1, 2, 3]
my_list.append(4)  # list is mutable
print("Modified list:", my_list)

name = "Alice"
# name[0] = "M"  # Error: strings are immutable
name = "M" + name[1:]  # create new string
print("New name:", name)


# 3. What is the difference between type conversion and type casting in Python?
# Ans:
# Type conversion: automatic conversion by Python (e.g., 10 + 2.5 becomes 12.5).
# Type casting: manual conversion by the programmer (e.g., int(), float()).


# 4. What data type is always returned from input() in Python, and how can it be used as a numeric type?
# Ans: input() always returns a string. You can convert it to int or float as needed.

# Example:
num = input("Enter a number: ")
num = float(num)
print("Number times 2:", num * 2)


# 5. What happens when multiple values are given inside the print() function?
# Ans: They are printed with spaces in between by default.

# Example:
print("Python", 101, 3.14)  # Output: Python 101 3.14
