# x=0

# if x<0:
#     print("value is negative")
# elif x==0:
#     print("value is equal to 0")
# else:
#     print("value is positive")

# num=int(input("enter a number"))

# if num>0:
#     print ("number is positive")
# elif num==0:
#     print("number is zero")
# else:
#     print("number is negative")

#ODD OR EVEN    
 
# num= int(input("enter a number"))
# if num %2==0:
#     print ("number is even")
# else:
#     print("number is odd")


#TRANSPOSED MATRIX

# def transpose_matrix(matrix):
#     transposed_matrix=[[matrix[j][i]
#     for j in range(len(matrix))] 
#     for i in range(len(matrix[0]))]
#     return transposed_matrix

# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# transposed=transpose_matrix(matrix)


# print("original matrix:")
# for row in matrix:
#     print(row)

# print("\nTransposed Matrix:")
# for row in transposed:
#     print(row)

# #2 Find a sum of all elements in a list

# numbers=[1,3,4,5,6]
# total_sum=sum(numbers)
# print (total_sum)

# #3 Write a program to implement List Comprehension

# numbers=[1,2,3,4,5,6,7,8,9]
# square=[x**2 for x in numbers]
# print(square)

#4 print largest and smallest numbers from list

# numbers=[10,15,30, 2, 5,7,45,9]

# largest=max(numbers)
# smallest=min(numbers)
# print("largest number is:",largest)
# print("smallest number is:",smallest)

#5 sqaures in first5 and last5

# sqauares=[x**2 for x in range(1,20)]

# first_5=sqauares[:5]
# last_5=sqauares[-5:]
# print("first 5 :" ,first_5)
# print("last 5 : ",last_5)

#6 Write a Python program to print the numbers of a specified list after removing even numbers from it

#using list c
# numbers=[1,2,3,4,5,6,7,8,9]
# odd=[i for i in numbers if i %2 !=0]
# print("if even number is removed answer:",odd)



# odd=list(filter(lambda x:x%2!=0,list1))
# print(odd)

#7 Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# def capitalize_input():
#     print("Enter lines of text (press Enter on an empty line to finish):")
    
#     lines = []
    
#     while True:
#         line = input()
#         if line == "":
#             break
#         lines.append(line.upper())
    
#     print("\nCapitalized lines:")
#     for line in lines:
#         print(line)

# # Call the function
# capitalize_input()

# Write a program to implement all built-in methods of list

#copy
lst = [1, 2, 3, 4, 5]
# lst_copy = lst.copy()
# print("Copy of list:", lst_copy)

#append
# lst.append(6)
# print("after adding 6:",lst)

#extend
# lst.extend([7,8])
# print("extending:",lst)

#insert
# lst.insert(0,1)
# print("inserting:",lst)

#remove
# lst.remove(3)
# print("after removing:",lst)

# 10) Define a class which has at least two methods one, to get a string from console  
# input and other is to print the string in uppercase

# class StringProcessor:
#     def __init__(self):
#         self.text = ""

#     def get_input(self):
#         self.text = input("Enter a string: ")

#     def print_uppercase(self):
#         if self.text:
#             print(self.text.upper())
#         else:
#             print("No input provided")


# processor = StringProcessor()
# processor.get_input()
# processor.print_uppercase()

# class MyClass:
#     # Class parameter
#     parameter = "Class parameter"

#     def __init__(self, parameter):
#         # Instance parameter
#         self.parameter = parameter

#     def show_parameters(self):
#         print(f"Class parameter: {MyClass.parameter}")
#         print(f"Instance parameter: {self.parameter}")

# # Example usage
# obj1 = MyClass("Instance parameter for obj1")
# obj2 = MyClass("Instance parameter for obj2")

# obj1.show_parameters()
# obj2.show_parameters()

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def compute_area(self):
#         # Area of a circle = π * r^2
#         return math.pi * (self.radius ** 2)

# # Example usage
# circle1 = Circle(5)
# circle2 = Circle(10)

# print(f"Area of circle with radius 5: ",circle1.compute_area())
# print(f"Area of circle with radius 10: ",circle2.compute_area())

# Define a class named BankAccount. This class should contain methods withdraw()
#  and deposit to calculate the balance amount remained in your account.

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self._account_number=account_number
#         self.__balance=balance

#     def _display_balance(self):
#         print("Balance:",self.__balance)
# b= BankAccount(123345,5000)
# b._display_balance()

# 13)Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have
#  a area function which can print the area of the shape where Shape's area is 0 by default. 

# class Shape:
#     def __init__(self):

#         pass

#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length

#     def area(self):
#         return self.length * self.length


# LOGIN page


import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Replace with actual authentication logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password")
app = tk.Tk()
app.title("Login Page")

# Create labels and entry widgets
label_username = tk.Label(app, text="Username")
label_username.pack(pady=5)
entry_username = tk.Entry(app)
entry_username.pack(pady=5)

label_password = tk.Label(app, text="Password")
label_password.pack(pady=5)
entry_password = tk.Entry(app, show="*")
entry_password.pack(pady=5)

# Create login button
button_login = tk.Button(app, text="Login", command=login)
button_login.pack(pady=20)

app.mainloop()