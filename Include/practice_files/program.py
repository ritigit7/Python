# import calendar
# print(calendar.month(2003,9))
# import random
# password=0
# pas=['a','d','r','h','3','j','s','5','h','p','y','o','l','k','b','r','6','e','x']
# for x in range(5):
#     password=password+random.choice(pas)[x]
# print(password)
# class a:
#     def __init__(self,name,age):
#         self.x=name
#         self.y=age
#     def f(self):
#         print(f"The name is :{self.x}\nage is :{self.y}")
# obj=a("ritik",19)
# obj.f()
# class a:
#     x=8
# obj=a
# print(obj.x)
# class list:
#     n=[]
#     def __init__(self,num):
#         self.n.append(num)
# for x in range(5):
#     x=int(input())
#     obj=list(x)
# print(obj.n)
# name="abc"
# class Employee:
#     empid=0
#     def __init__(self,id,name):
# 	    self.empid=id

# obj=Employee(5,"ritik")
# print(obj.empid)   
# class a:
#     t=9
#     def __init__(self):
#         a.t+=1
# print(a.t)
# obj=a()
# print(a.t)
class Student:
    schoolName = 'XYZ School' # class attribute

    def __init__(self): 
        self.name=''
        self.age=0
obj=Student()
obj.name="ritik"
print(obj.name)