class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class headptr:
    def __init__(self):
        self.head = None


def create(self):
    n = int(input("Enter the number of node:"))
    while(n > 0):
        value = int(input("Enter the data of node:"))
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node
        n = n-1


def p(self):
    temp = self.head
    while(temp != None):
        print(temp.data)
        temp = temp.next


first_node = headptr()

create(first_node)
p(first_node)
