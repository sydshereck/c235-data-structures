'''
    File name: Q2_array-based_stack.py
    Author: Sydney Shereck
    Student Number: 20207148
    Date: 1/21/2022
    Program: This code implements Stack class for an array based list.
    
'''

class Stack:
    def __init__(self):
        self.items = []
    # Returns amount of items currently in the stack.
    def size(self):
        return len(self.items)

    # Checks if stack contains any items.
    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    # Push adds an item to the top of the stack.
    def push(self, item):
        self.items.append(item)

    # Pop removes and returns the last item from the top of the stack.
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return ("IndexError: pop from empty list")

    # Top retrives the element at the top of the stack.
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return ("IndexError: top from empty list")

       
# Main Function to test
def main():
    test_stack = Stack()

    # Test pushing elements into stack
    # Expected output: [5, 'hello']
    test_stack.push(5) 
    test_stack.push("hello")
    print(test_stack.items) 

    # Test size and is_empty methods
    # Expected output: 2
    # Expected output: False
    print(test_stack.size())
    print(test_stack.is_empty())

    #Test top method
    # Expected output: hello
    print(test_stack.top())
    
    #Test poping elements from stack
    # Expected output: hello
    # Expected output: 5
    print(test_stack.pop())
    print(test_stack.pop())
    
    # Test top, pop and is_empty again on empty stack
    # Expected output: IndexError
    # Expected output: IndexError
    # Expected output: True
    print(test_stack.pop())
    print(test_stack.pop())
    print(test_stack.is_empty())

main()
    




