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

def transpose_matrix(matrix):
    transposed_matrix=[[matrix[j][i]
    for j in range(len(matrix))] 
    for i in range(len(matrix[0]))]
    return transposed_matrix

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transposed=transpose_matrix(matrix)


print("original matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)

#2 Find a sum of all elements in a list

numbers=[1,3,4,5,6]
total_sum=sum(numbers)
print (total_sum)

#3 Write a program to implement List Comprehension

numbers=[1,2,3,4,5,6,7,8,9]
square=[x**2 for x in numbers]
print(square)

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
numbers=[1,2,3,4,5,6,7,8,9]
odd=[i for i in numbers if i %2 !=0]
print("if even number is removed answer:",odd)



# odd=list(filter(lambda x:x%2!=0,list1))
# print(odd)