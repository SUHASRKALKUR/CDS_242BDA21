class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # Push an item onto the stack
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        # Remove and return the top item from the stack. Raises an error if the stack is empty.
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        item = self.stack.pop()
        print(f"Popped {item} from the stack.")
        return item

    def top(self):
        # Return the top item from the stack without removing it. Raises an error if the stack is empty
        if self.is_empty():
            raise IndexError("Peek from an empty stack.")
        return self.stack[-1]

    def is_empty(self):
        # Return True if the stack is empty, otherwise False
        return len(self.stack) == 0

    def size(self):
        # Return the number of items in the stack.
        return len(self.stack)

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    print(f"Top item is: {stack.top()}")
    print(f"Stack size is: {stack.size()}")
    stack.pop()
    stack.pop()
    print(f"Stack is empty: {stack.is_empty()}")
    stack.pop()
    stack.pop()
    print(f"Stack is empty: {stack.is_empty()}")


# Pushed 10 onto the stack.
# Pushed 20 onto the stack.
# Pushed 30 onto the stack.
# Pushed 40 onto the stack.
# Pushed 50 onto the stack.
# Top item is: 50
# Stack size is: 5
# Popped 50 from the stack.
# Popped 40 from the stack.
# Stack is empty: False
# Popped 30 from the stack.
# Popped 20 from the stack.
# Stack is empty: False