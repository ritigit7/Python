class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
class list_last:
    def __init__(self):
        self.last=None

class linked_list:

    def __init__(self):
        self.head = None

    def doubly_list(self):
        n = int(input("Enter the number of nodes:"))
        while(n > 0):

            val = int(input("Enter the value of node:"))
            new_node = node(val)
            if self.head == None:
                self.head = new_node
            else:
                last = self.head
                while(last.next != None):
                    last = last.next
                last.next = new_node
                new_node.prev = last
            n = n-1
        

    # def print_left(self):
    #    ptr=self.head
    #     while(ptr!=None):
    #         print(ptr.data,end=" ")
    #         ptr=ptr.prev

    def print_right(self):
        ptr=self.head
        while(ptr!=None):
            print(ptr.data,end=" ")
            ptr=ptr.next


first_node=linked_list()
first_node.doubly_list()
first_node.print_right()