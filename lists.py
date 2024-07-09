# List In Python 
'''
a = ["Name", 67 , 55 , 89.99]
b = [45,32,55,67,89]
c=[]

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# List Operations Adding lists
a=[23,45,67,89]
b=[12,34,65,76,87]
c=a+b
print(c)

# Replicating lists
a=[23,45,67,89]
print(a*3)

# Slicing Python Lists
list1 = [54, 14, 47, 89, 63, 21, 44, 28]
print(list1)
print(list1[4])
print(list1[0:5])
print(list1[2:6])
print(list1[-1:-3:-1])
print(list1[0:6:2]

# Updating List
data1 = [56, "india", "python", 45, 12, 22]
print(data1)
data1[1] = "india is great"
print(data1)
data1[3] = 99
data1[-1] = 100
print(data1) 

# Appending elements to the list
data=[56,"India","python"]
data.append(55)
data.append("Hello")
print(data) 

# Delete Elements
data1 = ["india", "python", 54, 12, 78, "australia"]
print(data1)
del data1[0]
print(data1)
del data1[1:4]
print(data1) 

# Built in Methods 

# 1. For minimum element min function 
list1 = [56, 43, 212, 17, 891, 90, 94, 34]
print("Minimum value in List 1 = %d" % min(list1))
# Error because we can’t compare STRING and INT
list2 = [45, 67, "Python", "India", 1]
print("Minimum value in List 2 = %d" % min(list2)) # Element should be of same data type for the min function to work. 

# 2 For maximum elemt max function 
list1 = [56, 43, 212, 17, 891, 90, 94, 34]
print("Maximum value in List 1 = %d" % max(list1)) 

list2 = [45, 67, "Python", "India", 1]
print("Minimum value in List 2 = %d" % max(list2)) 

# 3 Length of the list using len function 
list1 = [56, 43, 212, 17, 891, 90, 94, 34]
print("Length of the List 1 = " , len(list1)) 

# 4 Sum of the elements of list using sum function 
list1 = [56, 43, 212, 17, 891, 90, 94, 34]
a = sum(list1)
print("Sum of the List 1 = " , a)
list2 = [55, 66, 77, -88, 99]
print("Sum of the List 2 = " , sum(list2)) 

# 5 For getting the index value of the object 
list1 = ["python", 56, 123, "india", "hello", 56]
print("Index of 56 = %d" % (list1.index(56)))
print("Index of hello = %d" % (list1.index("hello")))
# Will give us error because 4545 is not in List
print("Index of 4545 = %d" % (list1.index(4545))) 

# 6 Python List count method 

list1 = ["python", 56, 123, "india", "hello", 56, 56]
print("56 has occurred %d times." % (list1.count(56)))
print("python has occurred %d times." %
(list1.count("python")))
print("4545 has occurred %d times." % (list1.count(4545))) 

# 7 Pop method to remove element
list1 = ["python", 56, 123, "india", "hello", 67, "world"]
print("Last Element removed is", list1.pop())
print(list1)
print("Third Element is and removed is", list1.pop(2))
print(list1) 

# 8 To insert objects at specified index 

list1 = ["python", 56, 123]
var = "hello"
list1.insert(1, var)
print(list1)

# 9 Adds element to last position if Position does not exists
list1.insert(10, 22)
print(list1) 

# 10 To extend the list further with another list
list1 = ["python", 56, 123]
list2 = [33, "Hello", "language"]
print(list1)
list1.extend(list2)
print(list1)
print(list2) 

# 11 Python List Remove object 
data1 = ['abc', 123, 10.5, 'a', 'xyz']
print(data1)
data1.remove(123)
print(data1)
# This will give us error because "python" is not in list
data1.remove(100) 

# 12 To reverse the elements in the list 
data1 = ['abc', 123, 10.5, 'a', 'xyz']
print(data1)
data1.reverse()
print(data1) 

# 13 Using sort method to sort 
data1 = [124,10.5,56,99,-23]
data1.sort()
print(data1) 


# Iterating over the list 
# 1 Using for loop
list1=[56,123,-56,2111,3]
for i in list1:
    print(i) 


# 2 Using for with range
list1=[56,123,-56,2111,3]
lenth=len(list1)
for i in range(lenth):
    print(list1[i]) 

# 3 Using in List
list1=[56,123,-56,2111,3]
for i in list1:
    print(i) 

# 4 Usinf while loop

list1=[56,123,-56,2111,3]
i=0
length=len(list1)
while i < length:
    print(list1[i])
    i+=1 ''' 

# Practice Problems 

# 1 
