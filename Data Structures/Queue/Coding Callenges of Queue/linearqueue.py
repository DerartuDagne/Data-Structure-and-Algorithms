# -*- coding: utf-8 -*-
"""LinearQueue.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1waqoG6xBryxK9kYnSiFd0UfXfNCdIyC1

Here's an implementation of a linear queue using a list in Python. In a linear queue, elements are added to the rear of the queue and removed from the front, following the First-In-First-Out (FIFO) principle. This implementation does not use a circular structure and thus can be simpler but might have inefficiencies if elements are frequently added and removed.
"""

class LinearQueue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity
        self.queue = [None] * capacity

    def enqueue(self, data):
        if self.size == self.capacity:
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty")
            return
        removed_element = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the slot for clarity
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return removed_element

    def display(self):
        if self.size == 0:
            print("Queue is Empty")
            return
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            print(self.queue[index], end=" <-- ")
        print()

    def front_element(self):
        if self.size == 0:
            print("Queue is Empty")
            return
        print("Front Element is:", self.queue[self.front])

# Driver code to test the LinearQueue class
if __name__ == "__main__":
    q = LinearQueue(4)

    print("Initial queue state:")
    q.display()  # Should print "Queue is Empty"

    print("Enqueueing elements:")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    print("Queue state after enqueue operations:")
    q.display()  # Should print the elements in the queue

    print("Attempting to enqueue when full:")
    q.enqueue(50)  # Should print "Queue is full"

    print("Dequeuing elements:")
    print("Removed:", q.dequeue())  # Should remove and print 10
    print("Removed:", q.dequeue())  # Should remove and print 20

    print("Queue state after dequeue operations:")
    q.display()  # Should print the remaining elements

    print("Enqueueing more elements:")
    q.enqueue(50)
    q.enqueue(60)

    print("Queue state after additional enqueue operations:")
    q.display()  # Should print the updated elements

    print("Front element of the queue:")
    q.front_element()  # Should print the current front element