# Generator

# def func():
#     yield 1
#     yield 2
#     yield 3
# x= func()
# for i in x:
#     print(i)

# def func():
#     for i in range(20):
#         if (i % 2==0):
#             yield i
# x=func()
# for i in x:
#     print(i)

# DECORATOR

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
# @make_pretty
# def ordinary():
#         print("I am ordinary")
# ordinary()


# def smart_divide(func):
#     def inner(a,b):
#         print ("I am going to divide",a,"and",b)
#         if b==0:
#             print("whoops! cannot divide")
#             return
#         return func(a,b)
#     return inner
# @smart_divide
# def divide(a,b):
#     print(a,b)
# divide(2,5)
# divide(2,0)


