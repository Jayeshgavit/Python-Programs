class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class linkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    
    def append(self, data):

        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
        
    def display(self):
        current = self.head 

        while current is not None:
            print(current.data, end=' ')
            current = current.next



a_list = linkedList();

n = int(input(" Enter a number of element add in list : "))

for i in range(n):
    data = input(f"Enter element : ")
    a_list.append(data)
print(' linked lsit is : ', end=' ');
a_list.display();