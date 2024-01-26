class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class list:
    def __init__(self):
        self.head = None

    def create(self):

        n = int(input("Enter the number of nodes:"))

        while(n > 0):
            val = int(input("node values:"))
            new_node = node(val)

            if(self.head == None):
                self.head = new_node
            else:
                temp = self.head
                while(temp.next != None):
                    temp = temp.next
                temp.next = new_node

            n = n-1


    def p(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next

    def search(self,val):
        i=1
        temp = self.head
        while(temp.data!=val):
            temp = temp.next
            i=i+1
        print(f"\n{i} is position of the node")

    def delete(self,val):
        temp2 = self.head
        while((temp2.next.data)!=val):
            temp2 = temp2.next  
        temp2.next=temp2.next.next 
        

list_l = list()
list_l.create()
list_l.p()
list_l.search(5)
list_l.delete(5)
list_l.p()