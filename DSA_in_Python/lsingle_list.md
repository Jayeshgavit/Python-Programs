Sure, let's go through this code with a detailed breakdown, including an example of adding elements step-by-step.

### 1. **Node Class**

The `Node` class represents each element (node) in the linked list. Each node has two attributes:
   - **`data`**: Stores the actual value of the node.
   - **`next`**: Points to the next node in the linked list. When the node is first created, `next` is set to `None` since it doesn't initially link to any other node.

#### Example:

```python
node1 = Node("apple")  # Creates a node with data "apple"
print(node1.data)  # Outputs: apple
print(node1.next)  # Outputs: None, since it doesn't link to any other node yet.
```

### 2. **LinkedList Class**

The `LinkedList` class manages the linked list, allowing us to add nodes and display the list's content. It has two main attributes:
   - **`head`**: Points to the first node in the linked list (initially `None` because the list is empty).
   - **`last_node`**: Points to the last node in the list, making it easier to add new nodes to the end.

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
```

#### Example:

```python
a_list = LinkedList()
print(a_list.head)  # Outputs: None, since the list is empty.
print(a_list.last_node)  # Outputs: None, since there's no last node in an empty list.
```

### 3. **Adding Nodes to the Linked List with `append` Method**

The `append` method lets us add new nodes to the end of the list.

1. **If the list is empty** (i.e., `self.head` is `None`), we:
   - Create a new node with the given data.
   - Set this new node as both the `head` and the `last_node`.

2. **If the list is not empty**:
   - Create a new node.
   - Set `last_node.next` to point to this new node (linking the current last node to the new node).
   - Update `last_node` to be the new node (now the new last element in the list).

```python
def append(self, data):
    if self.head is None:  # If the list is empty
        self.head = Node(data)
        self.last_node = self.head
    else:  # If the list is not empty
        self.last_node.next = Node(data)
        self.last_node = self.last_node.next
```

#### Example Walkthrough

Let's see how nodes are added step-by-step for this code:

1. **Create the Linked List**:
   ```python
   a_list = LinkedList()
   ```

   - `a_list.head` is `None`
   - `a_list.last_node` is `None`

2. **Append "apple"**:
   ```python
   a_list.append("apple")
   ```

   - Since `a_list.head` is `None`, the `append` method creates a new node with data `"apple"`.
   - This new node is set as both `head` and `last_node`.
   - So now:
     - `a_list.head.data` is `"apple"`
     - `a_list.last_node.data` is `"apple"`
     - `a_list.head.next` is `None` (since there's only one node in the list).

3. **Append "banana"**:
   ```python
   a_list.append("banana")
   ```

   - Since `a_list.head` is not `None`, the method creates a new node with data `"banana"`.
   - `a_list.last_node.next` is set to this new node (so the node with `"apple"` now points to `"banana"`).
   - `a_list.last_node` is updated to the new node with `"banana"`.
   - Now:
     - `a_list.head.data` is `"apple"`
     - `a_list.head.next.data` is `"banana"` (indicating "apple" points to "banana")
     - `a_list.last_node.data` is `"banana"`
     - `a_list.last_node.next` is `None`

4. **Append "cherry"**:
   ```python
   a_list.append("cherry")
   ```

   - A new node with data `"cherry"` is created.
   - `a_list.last_node.next` (which is the node with `"banana"`) is set to this new node, linking `"banana"` to `"cherry"`.
   - `a_list.last_node` is updated to the new node with `"cherry"`.
   - Now:
     - `a_list.head.data` is `"apple"`
     - `a_list.head.next.data` is `"banana"`
     - `a_list.head.next.next.data` is `"cherry"`
     - `a_list.last_node.data` is `"cherry"`
     - `a_list.last_node.next` is `None`

At this point, the linked list structure is as follows:

```
head -> "apple" -> "banana" -> "cherry" -> None
```

### 4. **Displaying the Linked List with `display` Method**

The `display` method prints each node’s data, starting from `head` and moving through each `next` pointer until it reaches a node with `next` as `None`.

1. A `current` variable starts at `self.head`.
2. **While `current` is not `None`**:
   - Print `current.data`.
   - Move `current` to the next node (`current = current.next`).

```python
def display(self):
    current = self.head 
    while current is not None:
        print(current.data, end=' ')
        current = current.next
```

#### Example

Using the previous list (`apple -> banana -> cherry`):

```python
a_list.display()
```

The `display` method will output:

```
apple banana cherry
```

### 5. **Complete Program Execution**

Putting it all together, the program performs these steps:

1. Prompts the user to enter the number of elements (`n`).
2. For each element:
   - Takes the input and appends it to the linked list.
3. After all elements are added, it displays the list content.

Here’s an example interaction:

```plaintext
Enter a number of elements to add in list: 3
Enter element: apple
Enter element: banana
Enter element: cherry
Linked list is: apple banana cherry
```

In summary:
- The program initializes an empty linked list.
- It adds elements to the list based on user input.
- Finally, it displays all elements in the order they were added, showing the linked list in its entirety.