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

    # Sum of alternate nodes
    def sum_alternate_nodes(self):
        temp = self.head
        total = 0
        position = 1

        while temp:
            if position % 2 != 0:
                total += temp.data

            temp = temp.next
            position += 1

        return total

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")

dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)
dll.insert(50)

dll.display()

result = dll.sum_alternate_nodes()
print("Sum of alternate nodes =", result)
