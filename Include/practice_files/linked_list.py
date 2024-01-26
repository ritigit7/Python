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

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked:
    def __init__(self):
        self.head=None

list=linked()
list.head=node(1)
n2=node(2)
n3=node(3)

list.head.next=n2
n2.next=n3

def p(self):
    temp=self.head
    while(temp!=None):
        print(temp.data)
        temp=temp.next

p(list)
print(list.head.next.data)