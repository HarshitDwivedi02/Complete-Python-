# While Loop 

#Example 1 
'''
count = 0
while count<9:
    print("The count is at : " , count)
    count += 1
print("End the count") 

# Using Break 
count = 0
while count < 9 :
    if count == 3:
        break
    print("The count is at :",count)
    count+=1
    
print("Good Bye!")

# Using if and continue 
count = 0
while count<9:
    count += 1
    if count == 4:
        continue
    print("The count is at:",count) 

# using nested while loop 

i=1
j=5

while i<4:
    while j<8:
        print(i ,",", j)
        i+=1
        j+=1 

# Practice Examples (While Loop Section)
# 1. Print first 10 natural numbers 
num=1
while num<=10:
    print(num,end=" ")
    num+=1 

# 2 Print all the even numbers from 1 to 100 
num=2
while num<=100:
    if num%2==0:
        print(num , end=" ")

    num+=1 

# 3 Find sum of n numbers where n is a user input 
sum=0
num=int(input())
i=1
while i<=num:
    sum+=i
    i+=1
    
print(sum)

# 4 Check prime or not 

num=int(input())

i=1
factor=0
while i<=num:
    if num%i==0:
        factor+=1
    
    i+=1
#if only 2 factors
if factor == 2:
    print("This is prime")
else:
    print("This is not prime")

# 5 Check Armstrong

n = int(input("Enter any number = "))
m = n
total = 0
while m > 0:
    digit = m % 10
    total = total + (digit ** 3)
    m = m // 10
if n == total:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

# 6 Find the factorial of a number 

num=int(input())
factorial=1
while num>0:
    factorial = factorial*num
    num-=1
print(factorial)

# 7 Print the 10 multiples of number 
num = int(input())
i=1
while i<=10:
    print(num*i)
    i+=1 

# 8 Count the number of digits 

num = int(input())
digits=0
while(num>0):
    n = num%10
    digits+=1
    num=num//10
print(digits)

# 9 Reverse a number 
num = int(input())
while num>0:
    digit = num%10
    print(digit, end="")
    num=num//10

# For Loop 
# 1 print first 10 natural no
for i in range(1,11):
    print(i)

# 2 Print all even from 1 to 100
for i in range(0,101,2):
    print(i, end=" ") 

# 3 Find sum of n number where n is user input

n=int(input())
sum=0
for i in range(1,n+1):
    sum = sum+i
    
print(sum)

# 4 Print multiplication table
n = int(input())
for i in range(1,11):
    print(n*i)''' 






        
    



    




