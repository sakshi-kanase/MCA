class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
        else:
            print("Popped element:", self.stack.pop())

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Top element:", self.stack[-1])

    def is_empty(self):
        return len(self.stack) == 0


# Main Program
s = Stack()

while True:
    print("\n--- STACK OPERATIONS ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Is Empty")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element to push: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        if s.is_empty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
