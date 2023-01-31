'''
    File name: Q2_linkedlist_stack.py
    Author: Sydney Shereck
    Student Number: 20207148
    Date: 1/21/2022
    Program: This code implements Stack class for a linked list.
    
'''
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    # Returns amount of items currently in the stack.
    def size(self):
        head = self.head
        size = 0
        while(head):
            size+=1
            head=head.next
        return size

    # Checks if stack contains any items.
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    
    # Push adds an item to the top of the stack.
    # If stack is empty makes item the head.
    def push(self, item):
        if not self.is_empty():
            node = Node(item)
            node.next = self.head
            self.head = node
        else:
            self.head = Node(item)
            
    # Pop removes and returns the last item from the top of the stack.
    def pop(self):
        if not self.is_empty():
            pop_item = self.head.item
            self.head = self.head.next
            return pop_item
        else:
            return ("IndexError: pop from empty list")

    # Top retrives the element at the top of the stack.
    def top(self):
        if not self.is_empty():
            top_item = self.head.item
            return top_item
        else:
            return ("IndexError: top from empty list")

       
# Main Function to test
def main():
    test_stack = Stack()

    # Test pushing elements into stack
    test_stack.push(5) 
    test_stack.push("hello")

    # Test size and is_empty method
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
    




