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
            print(current.data, end=' > ')
            current = current.next



a_list = linkedList();

n = int(input(" Enter a number of element add in list : "))

for i in range(n):
    data = input(f"Enter element : ")
    a_list.append(data)
print(' linked lsit is : ', end=' ');
a_list.display();








'''
### Summary: Linked List Implementation in Python

1. **Node Class**
   - Represents each element (node) in a linked list.
   - **Attributes**:
     - `data`: Holds the node’s value.
     - `next`: Points to the next node in the list (initially `None`).

2. **LinkedList Class**
   - Manages the list and provides methods to add and display nodes.
   - **Attributes**:
     - `head`: Points to the first node (initially `None`).
     - `last_node`: Points to the last node to simplify adding new nodes.

3. **Methods**
   - **`append(data)`**:
     - Adds a new node with the specified data to the end of the list.
     - If the list is empty, the new node becomes both `head` and `last_node`.
     - If not, links `last_node.next` to the new node and updates `last_node`.

   - **`display()`**:
     - Prints all nodes’ data in sequence from `head` to the last node.
     - Traverses the list until `current.next` is `None`.

4. **Program Flow**:
   - User inputs the number of elements and each element’s value.
   - Each element is added to the list with `append()`.
   - `display()` prints the linked list in the order of insertion.

5. **Example Execution**:
   - Input: 3 elements - "apple", "banana", "cherry".
   - Output: `apple banana cherry`.

'''