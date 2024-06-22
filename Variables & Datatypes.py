# Chapter 2 Data types , Variables etc

'''
a = "Hello World"
b = 27.8
c = 99.5

print(a)
print(b)
print(c)
print(b+c) 

# Multiple assignment
a,b,c = "Hello World",27.8,99.5
print(a)
print(b)
print(c)
print(b+c) 

# Data types
abc = "It's a string variable" # It is a string datatype variable
abc_1= 40 #It is a integer type
abc_2= 50.5 #It is a float type

print(abc_1+abc_2) 

# Determining data type
firstname = "John Doe"
age = 32

print(type(firstname))
print(type(age)) 

# Arithmetic operations can not be performed on string
var1 = "Hello"
var2 = 4
print(var1 + var2) 

# Two Strings can be concatenated into one string 
string1 = " Hello "
string2 = " I am Harshit "
string3 = string1+string2
print(string3) 

# Typecasting in Python:
abc = 5
abc2 = '45'
abc3 = 55.95
xyz = 5.0
abc4 = int(abc2)
print(abc + abc4)
print(abc + int(abc2))
print(float(abc) + xyz) 

# Input Function in Python:
print("Enter your name : ")
name = input() # It will take input from user
print("Your Name is", name) # It will show the name
xyz = input("Enter your age : ")
print("Your age is", xyz) 

# Taking number in the input 
a = input("Enter number 1 = ")
b = input("Enter number 2 = ")
print(a + b) # It gives error as it gives string as input and strings get concatenated 

a = input("Enter number 1 = ")
b = input("Enter number 2 = ")
c = int(a)
d = int(b)
print(c + d) # It gives correct output as we typecast the variables into integer 

a = int(input("Enter number 1 = "))
b = int(input("Enter number 2 = "))
print(a + b) # This will also give right output as we typecast at start only '''



