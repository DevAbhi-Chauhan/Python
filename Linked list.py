class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Deletion by value
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # Traversal and printing the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list
my_list = LinkedList()

# Insertion
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

# Display the list
print("Linked List:")
my_list.display()

# Deletion
my_list.delete(3)

# Display the list after deletion
print("Linked List after deleting 3:")
my_list.display()

# In this implementation:

# 1. Node represents an individual element in the linked list, containing data and a reference to the next node.
# 2. LinkedList represents the linked list itself and includes methods for insertion (append), deletion (delete), and traversal (display).