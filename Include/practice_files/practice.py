# #this program for Enter name and date
# latter='''
# Dear <|Name|>
#         you are selected
#     Date:<|Date|>
# '''
# name=input("Enter Your Name:")
# date=input("Enter today date:")
# latter=latter.replace("<|Name|>",name) # do this  because we save replace in latter
# latter=latter.replace("<|Date|>",date)
# print(latter)
# #from here

# #finding doubke space
# string="This program is for  deteting 2 charecter"
# print(string[0::3])
# print(string.find("  "))
# print(string.replace("  "," "))
# #from here

# #Edit string 
# lat="Dear Ritik,\n\tthis is nice Python Program. \n\t\tThanks."
# print(lat)
# # from here

# #practice for sorting 3 number
# a1=input("Enter number:")
# a1=int(a1)
# print(a1)

# a2=input("Enter number:")
# a2=int(a2)
# print(a2)

# a3=input("Enter number:")
# a3=int(a3)
# print(a3)

# b=[a1,a2,a3]
# b.sort()
# print(b)
# b.reverse()
# print(b)
# #from here

# c=[1,4,5,3,2,2]
# d=(1,4,5,3,2,2)
# print(c.count(2))
# print(d.count(2))

# #Practice 
# a1=input("Enter the fruit name:")
# a2=input("Enter the fruit name:")
# a3=input("Enter the fruit name:")
# a4=input("Enter the fruit name:")
# a5=input("Enter the fruit name:")
# a6=input("Enter the fruit name:")
# a7=input("Enter the fruit name:")
# b1=[a1,a2,a3,a4,a5,a6,a7]
# print(b1)
# # from here

#practice 
# m1=input("enter the student mark :")
# m2=input("enter the student mark :")
# m3=input("enter the student mark :")
# m=[m1,m2,m3]
# m.sort()
# print(m)
# m=(m1,m2,m3)
# m[1]=20
# print(m)
#from here

#practice
# n=[2,3,6,7,1]
# print(sum(n))
# print("The sum of number is: ",n[0]+n[1]+n[2]+n[3]+n[4])
# print(n.count(1))
#from here

# practice
# a=input("Enter naumber:")
# b=input("Enter naumber:")
# a=int(a)
# b=int(b)
# print(a+b)
# c=int(input("Enter name:"))
# d=int(input("Enter name:"))
# print(c+d)

# practice
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# c=int(input("Enter the number:"))
# d=int(input("Enter the number:"))
# if(a>b):
# def fun(n):
#     print(5+n)
# class Warehouse:
#    purpose = 'storage'

# w1 = Warehouse()
# print(w1.purpose, w1.region)

# w2 = Warehouse()
# w2.region = 'east'
# print(w2.purpose, w2.region)

# w1 = Warehouse()
# print(w1.purpose, w1.region)
# def f1(x, y):
#     return min(x, x+y)

# class C:
#     f = f1

#     def g(self):
#         return 'hello world'
    # h = g
# obj=C
# print(obj.f(5,3))
# print(obj.g)
# print(obj.h)
# class Bag:
#     def __init__(self):
#         self.data = []

#     def add(self, x):
#         self.data.append(x)

#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)
# obj=Bag()
# obj.add(obj,7)
# obj.addtwice()
# print
