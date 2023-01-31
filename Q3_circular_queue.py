'''
    File name: Q3_circular_queue.py
    Author: Sydney Shereck
    Student Number: 20207148
    Date: 1/21/2022
    Program: This code implements a Queue ADT, storing elements in a circle.
    
'''

class CircularQueue:
    # Initialization function takens int value x as input.
    # Variable x determines capacity of circular queue.
    def __init__(self, x):
        self.x = x
        self.queue = [None] * x
        self.head = -1
        self.tail = -1
        self.count = 0

    def is_empty(self):
        if self.tail == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.tail == (self.x - 1):
            return True
        else:
            return False
        
    # Enqueue function takes an element and inserts into the queue.
    def enqueue(self, item):
        if self.is_full():
            print("Cannot enqueue item; circular queue is full")
        else:
            self.queue[self.tail] = item
            self.tail += 1

    def dequeue(self):
        if self.queue[self.head] == None:
            print("Cannot dequeue item; circular queue is empty")
        else:
            top = self.queue[self.head]
            self.queue[self.head] = None
            self.head += 1 
            if self.head == self.x +1:
                self.head = 0
            return top

# Main Function to test.
def main():
    test_queue = CircularQueue(5)

    # Test enqueue elements into queue.
    # No expected output.
    test_queue.enqueue(1)
    test_queue.enqueue(2)
    test_queue.enqueue(3)
    test_queue.enqueue(4)
    test_queue.enqueue(5)
    
    # Enqueue element above maximum capaicty.
    # Expected output: Cannot enqueue item; circular queue is full.
    test_queue.enqueue(6)

    # Test dequeue elements from queue.
    # Expected output: 1, 2, 3, 4, 5.
    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.dequeue())

    # Dequeue element from empty queue.
    # Expected output: "Cannot dequeue item; circular queue is empty".
    test_queue.dequeue()
    
main()
    




