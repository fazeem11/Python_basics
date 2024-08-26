#super function

# class A:
#     def func1(self):
#         print("function one working")
#     def func(self):
#         print("function working from class A")

# class B(A):
#     def func3(self):
#         print("function 3 worling")
#     def func(self):
#        print("function working from class B" )
#        super().func()

# obj = B()  
# obj.func() 

# #Public

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("Name:",self.name)
#         print("age:self.age")
# s = Student ("john",20)
# s.display()

#Private

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.__account_number=account_number
#         self.__balance=balance

#     def __display_balance(self):
#         print("Balance:",self.__balance)

# b= BankAccount(123345,5000)
# b.__display_balance()

#Protected

# class person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def _display(self):

#         print("name:", self._name)
#         print("age:", self._age)

# class student(person):
#     def __init__(self,name,age,rollnumber):
#         super().__init__(name,age)
#         self._roll_number=rollnumber
#     def display(self):
#         self ._display()
#         print("Roll number:",self._roll_number)
# s=student("john",20,56)
# s.display()
