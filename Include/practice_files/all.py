# print(r"a:\new")
# a=2
# b=3
# print(id(a),id(b))
# if a is b:
#     print(a)
# else:
#     print(b)
# c=5
# print("the value of a is",a,"my name is",c)
# print("the value of a is "+str(a)+" my name is "+str(c))
# print(f"the value of a is {a} my name is {b}")
# print("the value of a is {} my name is {}".format(a,b))
# print("the value of a is {1} my name is {0}".format(a,b))
# print("the value of a is {n} my name is {m}".format(n=a,m=b))

# print(input("Name:"))
# a,b=4,8
# print(a,b)
# a,b = 10,20
# b = a + b
# print("Sum = ", b)
# print((8>>4)<<4)
# a="ritik"
# if "a" in a:
#     print("ok")
# else:
#     print("no")

# str="Hello World"
# for x in str:
#     print(x)

# str=" asdfgh,jvcxz "
# # print(str[0::3])
# print(len(str))
# print(str.strip())
# print(str.replace("f","F"))
# print(str.split("f"))
# print(str)
# str = "The words present in this string are separated by white space."
# print(len(str.split()))

# num=[29,53,22,13]
# print(num)
# a=["ritik",4.2,5]
# print(a[1])
# print(type(a))
# for x in a:
#     print(x)
# print(a[-3:-1])
# a[3]=64
# print(len(a))
# t=(10,20)
# a=[10,10,24]
# print(t[1])
# t[1]=2
# print(a.index(10))
# a = ['*', '**', '***', '****', '*****', '******']
# for x in a:
#     print(x)
# data={"a":5,"b":"name"}
# data["c"]=["ritik",3,2.4]
# for a in data:
#     print(a,data[a])
# print(data["c"][1])
# data.pop("a")
# print(data)
# del data["a"]
# print(data)

# data = {"apple": 250, "orange": 300, "mango":50, "banana": 100}
# Write your code here
# fruits.pop("mango")
# print(fruits)
# c=fruits.copy()
# c=data
# data={10,200,50,10}
# x=int(input())
# for x in data:
#     print(x)
# a=input("enter numbe")
# print(a)
# data= {'a', 'e', 'i', 'o', 'u'}
# Write your code here
# a = input()
# for x in vowels:
#     if(a is x):
#         print("Yes")
#     else:
#         print("No")
# data={10,20,30,40}
# data.update({23,21,53})
# data.clear()
# print(data)
# data = {10, 200, 100, 500, 2000}
# Write your code here
# a=int(input())
# data.discard(a)
# print(data)
# a={10,23,42}
# b={20,21,12}
# print(a.union(b))
# print(a.intersection(b))
# str="abcdefghijklmnop"
# for x in str:
#     print(x)

# list=[1,2,3,4,5]
# for x in list:
#     print(x)

# tuple = (1, 2, 42, 4, 1)
# for x in tuple:
#     print(x)

# dictonary = {
#     "a": 3,
#     "b": 2,
#     "c": {"s": 5,"d": 9,"g": 8},
#     "d": 6,
# }
# # for x in dictonary:
# # print(dictonary[x])
# print(dictonary["c"]["s"])

# set={2,4,2,6,7}
# print(set)
# for x in set:
#     print(x)
# t=0
# a=input()
# v="aeiou"
# for x in a:
#     for y in v:
#         if y is x:
#             t=t+1
# print(t)
# data="lfkjieojkdsfirfkj"
# print(data[::2])

# for x in range(3, 15, 4):
#     print(x)
# for x in range(0,100,2):
#     print(x)
# n=int(input())
# while n>0:
#     print(n)
#     n=n-1
# n = (str)(input())
# i = len(n)-1
# s=0
# while i >= 0:
#     s=s+(int)(n[i])
#     i = i-1
# print(s)
# j=0
# while j>0:
#     print("*",end=' ')
#     j=j+1
# numberrows=int(input())
# f = 1
# while(f <= numberrows):
#     g = 1
#     while g <= f:
#         print(("*"), end=" ")
#         g = g + 1
#     f = f + 1
#     print()

# print("*",end='')
# print("*")

# a=[1,2,3,4,5]
# for x in a:
#     print(x)
#     if x==3:
#         break
# else:
#     print("Ok")
# print("ok")

# def fun(n,m):
#     print(n*m)
# n=int(input())
# m=int(input())
# fun(n,m)

# def fun():
#     display(a, b, c)


# def display(a, b, c):
#     print(a*b*c)
# fun()
# def display(a,b,c=5):
#     print(a+b+c)
# display(1,4)

# a=[1,3,4,5]
# for x in range(0,10):
#     for y in range(x):
#         print("*",end='')
#     print()

# def fact(n):
#     if(n == 0):
#         return 1
#     else:
#         return n*fact(n-1)
# n = int(input())
# print(fact(n))

# def sum(*data):
#     s=0
#     for x in data:
#         s=s+x
#     print(s)
# sum(4,6,3)

# def fun():
#     print("ritik")
#     return 19==54
# # a,b=fun()
# print(type(fun()))
# print(fun())
# def a(x, y):
#     return x**y
# print(a(4, 2))

# def fun(n):
#     return lambda x: x**n
# s = fun(4)
# print(s)

# def add(a):
#     return a+5
# def cal(f,n):
#     return f(n)
# n=3
# print(cal(add,n))

# f=open("D:\python\python programs\data.txt","r")
# print(f.read())
# print(f.readline(),end="")
# f.close()

# f=open("data1.txt","w")
# f.write("ritik maurya\n")
# f.write("abcdefghijklmnopqrstuvwxyz")
# f.close()
# f=open("data1.txt","r")
# print(f.read())
# f.close()
# print(type(f))

# class student:
#     def data(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number
# s1 = student()
# s2 = student()
# s1.data("ritik", 77)
# s2.data("abcd", 32)
# print(s1.name, s1.roll_number, s2.name, s2.roll_number)
# print(s1)

# class Sample:
#     def __init__(self):
#         print("Hello World")
# a=Sample()
# Sample.hello()
# a.hello()


# class Data:
#     def setData(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def getData(self):
#         print(f"x={self.x}\ny={self.y}\nz={self.z}")

# obj = Data()
# obj.setData(10, 20, 30)
# obj.getData()

# class Data:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def getData(self):
#         print(f"x={self.x}\ny={self.y}\nz={self.z}")
# obj=Data(10, 20, 30)
# obj.getData()

# x,y=5,3
# print(x,y)

# def fun():
#     global x
#     x=5
#     print(x)
# fun()
# print(x)

# class examle:
#     commen=50
#     def __init__(self,val):
#         self.local=val
# A=examle(10)
# B=examle(20)
# print(A.commen,A.local)
# print(B.commen,B.local)

# class list:
#     n = []

#     def __init__(self, num):
#         self.n.append(num)

# for x in range(1, 6):
#     obj = list(x)
# print(obj.n)

# class s_c_data:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#         self.__password = 221011

#     def fun(self):
#         return self.__password

# class s_l_data(s_c_data):
#     def __init__(self, name, roll_no, date, book):
#         s_c_data.__init__(self, name, roll_no)
#         self.date = date
#         self.book = book


# o = s_l_data("ritik", 77, 5, "abc")
# print(o.__password)
# print(o.fun())


# class x:
#     def __init__(self,a,b):
#         self.c=a
#         self.d=b
# y=x(5,7)
# print(y.c)

# class A:
#     def __init__(self, a):
#         print(a)
# class B:
#     def __init__(self, b):
#         print(b)
# class C(A,B):
#     def __init__(self, c,a,b):
#         A.__init__(self, a)
#         B.__init__(self, b)
#         print(a+b)
# obj=C(4,3,6)

# class A:
#     def __init__(self, a):
#         print(a)
# class B(A):
#     def __init__(self, b,a):
#         A.__init__(self, a)
#         print(b,a)
# class C(B):
#     def __init__(self, c,a,b):
#         B.__init__(self, b,a)
#         print(c,a,b)
# obj=C(3,5,2)

# from math import pi
# print(pi)

# import test
# test.f1(5)

# import test
# test.f1(5)
# obj=test.f1
# obj(4)

# import test as t
# t.f1(5)
# from test import f2
# f2(4)

# from test import *
# f2(5) #here no need to use test.f2

# import test 
# obj=test
# obj.f1(4)
# i=0
# while(i<5):
#     print()
# i=9
# print(type(i))