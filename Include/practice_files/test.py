# def f1(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")
# def f2(n):
#     print(n-2,n+3)
# print("\U0001F917")
# m=[x for x in range(5)]
# m=[]
# for x in range(5):
#    m.append(x)
# print(m)
# l=[8,0,5,4,1,6]
# l.sort()
# print(l)
# print(l.index(2))
# l = []
# n = int(input("size:"))
# for x in range(n):
#     t = int(input("n"+str(x+1)+":"))
#     l.append(t)
# print(l)
# class a:
#     def s(self):
#         l.sort()
#         print(l)

#     def check(self):
#         if l.index(self) < n:
#             print(str(self)+"is avialable in list")
# obj=a()
# obj.s()
# def blub():
#     a = list()
#     a.append(1.0)
#     return a
# print(blub())
# print(a)
# def blub():
#     a = list([1])
#     a.append(1.0)
#     return a
# print(blub())
# at=1,2,3
# a,b,c=at
# print(a)
# import sql_by_python
# sql_by_python.mycorsor.execute("select * from c")
# import numpy as np
# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)
# import random
# l=[1,2,3,4,5,6,7,8,9]
# s="ridsfnekjd"
# t=".<>/?';}[=_+"
# a="abcdefghijklm"
# n=random.choice(l)
# m=random.choice(s)
# o=random.choice(t)
# p=random.choice(a)
# n.round(2)
# l.append(n)
# q=[]
# q.append(str(n)+m+o+p)

# print(str(n)+m+o+p)
# print(q)
# print(sorted(l))
# a=(1,2,3,4,5)
# b=(4,5,6,7,8)
# print(len(a-b))
# from datetime import *
# from datetime import datetime
# now = datetime.now()
# now.strftime("%m/%d/%Y, %H:%M:%S")
# print(now)
# import turtle
# import math
# print(dir(turtle))
# import mariadb
# print(dir(mariadb))
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print(self):
#         temp = self.head
#         while (temp):
#             print(temp.data, end=" ")
#             temp = temp.next


# if __name__ == "__main__":

#     llist = LinkedList()

#     llist.head = Node(10)
#     middle = Node(20)
#     last = Node(30)

#     llist.head.next = middle
#     middle.next = last

#     print("The LinkedList Elements Are:")
#     llist.print()
# from pytube import *
# list="https://youtu.be/_PuIzVqJJbA"
# yt=YouTube(list)
# yt.streams.first().download()
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print(self):
#         temp = self.head
#         while (temp):
#             print(temp.data, end=" ")
#             temp = temp.next

# llist = LinkedList()
# llist.head = Node(10)
# middle = Node(20)
# last = Node(30)
# llist.head.next = middle
# middle.next = last
# print("The LinkedList Elements Are:")
# llist.print()

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class list:
#     def __init__(self):
#         self.head = None

#     def prin(self):
#         temp = self.head
#         while(temp!=None):
#             print(temp.data,end=' ')
#             temp=temp.next


# print("Enter size:")
# n=int(input())

# object=list()
# print("Enter number:")
# object.head=node(int(input()))

# i=0
# while(i<n):
#     temp=node(int(input()))
#     if(i==0):
#         object.head.next=temp
#     else:
        

# object.head=node(40)
# o2=node(20)
# o3=node(10)
# o4=node(30)
# object.head.next=o2
# o2.next=o3
# o3.next=o4
# o4.next=None
# object.prin()
# def p(n):
#     i=0
#     while(i<n):
#         print(i)
#         i+=1
# p(5)
# def i():
#     return ("the ....")
# print(i())
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def addLast(self, val):
#         newNode = Node(val)

#         if self.head == None:
#             self.head = newNode
#         else:
#             lastNode = self.head

#             while lastNode.next != None:
#                 lastNode = lastNode.next
            
#             lastNode.next = newNode

#     def printList(self):
#         temp = self.head
#         print("The LinkedList Elements Are:")
        
#         while(temp):
#             print(temp.data)
#             temp = temp.next


# if __name__ == "__main__":

#     llist = LinkedList()

#     print("Inserting Element: 10")
#     llist.addLast(10)

#     print("Inserting Element: 20")
#     llist.addLast(20)

#     print("Inserting Element: 30")
#     llist.addLast(30)

#     llist.printList()
def p():
    print("dslkjfka")

def d():
    print("weih")
    p()

d()