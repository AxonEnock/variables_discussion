## 1. What is a Variable?
# A variable is a name that stores a value in memory. 
# It allows us to store and manipulate data in Python programs.

## Declaring and Assigning Variables
# In Python, you declare and assign a variable using the = (assignment) operator.

# EX
# x = 10  # x is assigned the value 10
# y = "Hello, Sylvester!"  # y is assigned a string value
# z = 3.14  # z is assigned a floating-point number

# Python is dynamically typed, 
# meaning you don’t have to declare the type of a variable explicitly.


## Variable Naming Conventions
# Must start with a letter (a-z, A-Z) or an underscore _
# Cannot start with a number
# Can contain letters, numbers, and underscores
# Cannot be a Python keyword (if, for, while, class, etc.)
# Should be concise and follow naming best practices

## Dynamic Typing in Python
# Python allows you to change the type of a variable on the fly.?

# EX
# a = 10     # a is an integer
# a = "Now is a string"  # Now a is a string
# a = 3.5    # Now a is a float

# This is different from statically typed languages like Java or C, 
# where you must declare types explicitly.












## 2. Variable Types in Python
# Python has different data types to classify variables. The main ones are:

# Integer (int) – Whole numbers
# Floating-point (float) – Decimal numbers
# String (str) – Text
# Boolean (bool) – True or False
# NoneType (None) – Represents the absence of a value


## A. Integer (int)
# Used for whole numbers, both positive and negative.

# EX
# age = 18
# year = 2025
# temperature = -5
# print(type(age))  # Output: <class 'int'>

## B. Floating-Point (float)
# Used for decimal numbers.

# EX
# pi = 3.1416
# height = 5.9
# distance = -20.45
# print(type(pi))  # Output: <class 'float'>



## C. String (str)
# A sequence of characters enclosed in single (') or double (") quotes.?

# EX
# name = "Sylvester"
# greeting = 'Hello, World!'
# message = "It's a great day!"
# print(type(name))  # Output: <class 'str'>

## D. Boolean (bool)
# Has only two values: True or False.

# EX
# is_student = True
# passed_exam = True
# print(type(is_student))  # Output: <class 'bool'>

#💡 Booleans are often used in conditions:

# EX
# x = 10
# y = 5
# print(x > y)  # Output: True
# print(x == y)  # Output: False

## E. NoneType (None)
# Used when a variable has no value.

## Checking Data Types
# You can use type() to check a variable's type.

# EX
# x = 25
# print(type(x))  # Output: <class 'int'>
# y = "Hello"
# print(type(y))  # Output: <class 'str'>

## Type Conversion (Casting)
# Python allows converting one type into another.

# EX
# Convert int to float
# x = 10
# x = float(x)  
# print(x)  # Output: 10.0
# Convert float to int
# y = 3.99
# y = int(y)  
# print(y)  # Output: 3  (decimal part removed)
# # Convert string to int
# z = "100"
# z = int(z)  
# print(z)  # Output: 100
# Convert number to string
# num = 25
# num = str(num)  
# print(num)  # Output: "25"
# Convert boolean to int
# print(int(True))   # Output: 1
# print(int(False))  # Output: 0












## 4. Working with Numbers in Python
# Python supports different types of numbers:

# Integers (int) – Whole numbers
# Floating-point (float) – Decimal numbers
# Complex numbers (complex) – Numbers with an imaginary part


# EX

# x = 10
# y = 3

# print(x + y)   # Addition → 13
# print(x - y)   # Subtraction → 7
# print(x * y)   # Multiplication → 30
# print(x // y)  # Floor division → 3 (ignores decimals), truncation
# print(x % y)   # Modulus (remainder) → 1
# print(x ** y)  # Exponentiation (power) → 1000 (10^3)









### . String Indexing & Slicing
# Each character in a string has an index:

#     S  y  l  v  e  s  t  e  r
#     0  1  2  3  4  5  6  7  8
#    -9 -8 -7 -6 -5 -4 -3 -2 -1

# Indexing (Accessing a Character)

# EX
# name = "Sylvester"
# print(name[3])  # Output: S
# print(name[-1]) # Output: r

# Slicing (Extracting a Part of a String)

# EX
# word = "Robotics"
# print(word[0:3])  # Output: Rob  (0 to 2, index 3 is excluded)
# print(word[:4])   # Output: Robo (Starts from 0)
# print(word[4:])   # Output: tics (Goes till the end)
# print(word[:-3])  # Output: ics  (Last 3 characters)
# print(word[-3:])



#Asht that it for variables.