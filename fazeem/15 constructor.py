#create class
 
# class Myclass:
#     x=5
# #print(Myclass)    

# #object

# ob1=Myclass()
# print(ob1.x)

#constructor (__init__())

# class Employee:
#     def __init__(self,name="bhavana",age=24):
#         self.name=name
#         self.age=age
#     def displayEmployee(self):
#              print("name:",self.name,",age:",self.age)

# e1=Employee()
# e2=Employee("Bharat",25)

# e1.displayEmployee()
# e2.displayEmployee()

class Employee:
    def __init__(self,name="bhavana",age=24):
        self.name=name
        self.age=age
        print("name:",self.name,",age:",self.age)

e1=Employee()
e2=Employee("Bharat",25)
