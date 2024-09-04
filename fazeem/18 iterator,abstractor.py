# iter

# class Numbers:
#     def __iter__(self):
#         self.a =1
#         return self
    
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass = Numbers()
# myiter=iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Abstract

# from abc import ABC,abstractmethod
# class car(ABC):
#     def mileage(self):
#         pass

# class tesla(car):
#     def mileage(self):
#         return super().mileage()
#     print("the mileage is 30kmph")
# class suzuki(car):
#     def mileage(self):
#          print("the mileage is 24kmph") 
# class porsche(car):
#     def mileage(self):
#         return super().mileage()
#     print("the mileage is 25kmph")
    
# t=tesla()
# t.mileage()
# r=porsche()  
# r.mileage()
# s=suzuki()
# s.mileage()  

