# -*- coding: utf-8 -*-
"""QueueUsingStacks.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15gosvybTxKiIWqpdScKDoLsB9w_8jkeF

QueueUsingStacks is a design pattern where two stacks are used to implement the functionality of a queue. This approach leverages the stack's Last-In-First-Out (LIFO) property to emulate the queue's First-In-First-Out (FIFO) behavior.
"""

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # Add item to stack1
        self.stack1.append(item)

    def dequeue(self):
        # Move elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop from stack2
        if not self.stack2:
            raise IndexError("Dequeue from empty queue")
        return self.stack2.pop()