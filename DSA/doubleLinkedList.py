class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Update a node value
    def update(self, old_data, new_data):
        temp = self.head

        while temp:
            if temp.data == old_data:
                temp.data = new_data
                print(f"{old_data} updated to {new_data}")
                return
            temp = temp.next

        print("Value not found!")

    # Delete a node
    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Deleting head node
        if temp.data == data:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print(f"{data} deleted")
            return

        while temp:
            if temp.data == data:

                # Link previous node to next node
                if temp.prev:
                    temp.prev.next = temp.next

                # Link next node to previous node
                if temp.next:
                    temp.next.prev = temp.prev

                print(f"{data} deleted")
                return

            temp = temp.next

        print("Value not found!")

    # Display list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        print("Doubly Linked List:", end=" ")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

dll = DoublyLinkedList()

# Insert elements
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)

print("After Insertion:")
dll.display()

# Update element
dll.update(20, 25)

print("\nAfter Update:")
dll.display()

# Delete element
dll.delete(30)

print("\nAfter Deletion:")
dll.display()
