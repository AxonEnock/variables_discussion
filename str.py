## 1. Introduction to Strings

# What are strings?
# A string is a sequence of characters enclosed in quotes. 
# Strings can include letters, numbers, symbols, and whitespace.

## Creating strings
# Strings in Python can be created using:

# Single quotes ('...')
# Double quotes ("...")
# Triple quotes ('''...''' or """...""") (for multi-line strings)

# EX

# # Single-quoted string
# name = 'Sylvester'
# # Double-quoted string
# greeting = "Hello, world!"
# # Triple-quoted string (for multiple lines)
# poem = '''Roses are red, 
# Violets are blue, Python is fun, 
# And so are you.'''
# print(name)
# print(greeting)
# print(poem)











## 2. String Basics

## Accessing Characters (Indexing)
# Strings are indexed, meaning each character has a position (starting from 0).
# Python allows positive indexing (left to right) and negative indexing (right to left).

# EX
# word = "Python"
# # Positive indexing (starts from 0)
# print(word[0])  # P
# print(word[3])  # h
# # Negative indexing (starts from -1)
# print(word[-1])  # n
# print(word[-4])  # t


## Slicing strings
# We can extract parts of a string using slicing:
# ie
# string[start:end] → Extracts from start to end-1.
# string[start:end:step] → Steps through the string.

# EX.1
# text = "Hello, Python!"
# Basic slicing
# print(text[0:5])   # Hello
# print(text[7:13])  # Python
# Omitting start or end
# print(text[:5])    # Hello (from start)
# print(text[7:])    # Python! (to the end)
# # Using a step
# print(text[::2])   # Hlo yhn
# print(text[::-1])  # !nohtyP ,olleH (reversed string)


 
# # EX.2
# text = "Hello, World!"
# # Basic slicing (start:end)
# print(text[0:5])  # Hello (characters from index 0 to 4)
# print(text[7:12]) # World (characters from index 7 to 11)
# # Omitting start and end
# print(text[:5])   # Hello (from the start to index 4)
# print(text[7:])   # World! (from index 7 to the end)
# # With step
# print(text[::2])  # Hoo ol! (every second character)

# # EX.3
# text = "Hello, World!"
# # Negative slicing
# print(text[-6:-1])  # World (from index -6 to -2)
# print(text[-6:-1:-1])  # !dlroW (from the end to index -6, reversing)




## String length (len())
# The len() function returns the length of a string (number of characters).

# EX
# text = "Python"
# print(len(text))  # 6











## 3. String Operations
# Python allows various operations on strings, 
# such as concatenation, repetition, and comparison.

## String concatenation (+)
# You can combine (concatenate) strings using the + operator.

# EX
# first_name = "Sylvester"
# last_name = "Enock"
# full_name = first_name + " " + last_name  # Adding a space in between
# print(full_name)  # Sylvester Enock

## Note: You cannot concatenate a string with a number directly. 
# You must convert numbers to strings first.

# EX
# age = 19
# message = "I am " + str(age) + " years old."
# print(message)  # I am 19 years old.

## String repetition (*)
# The * operator repeats a string multiple times.

# EX
# laugh = "Ha! "
# print(laugh * 100)  # Ha! Ha! Ha! 


## String comparison (==, !=, <, >, etc.)
# Strings can be compared using relational operators.

# EX
# print("apple" == "apple")  # True
# print("banana" != "apple")  # True
# print("car" > "bus")  # True (alphabetically, 'c' > 'b')
# print("dog" < "elephant")  # True
# print(5 > 2)
# print("hello" == "Hello")





# 🔹 Note: Comparisons are case-sensitive, meaning "Hello" is not equal to "hello".



