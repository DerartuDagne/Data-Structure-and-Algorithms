# -*- coding: utf-8 -*-
"""CircularQueue.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bMbQ3AdfZVqJ9adF0Den5FCHF3T7m1cV

The concept of a circular queue is an extension of the standard queue data structure that uses a fixed-size array in a circular manner to manage the elements. Unlike a linear queue, where once the end of the array is reached, it can no longer accept new elements, a circular queue allows for efficient use of space by wrapping around to the beginning of the array when it reaches the end. This approach is particularly useful in scenarios where the queue might frequently wrap around, such as in buffering applications.
"""

class CircularQueue:
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
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return removed_element

    def display(self):
        if self.size == 0:
            print("Queue is Empty")
            return
        index = self.front
        for _ in range(self.size):
            print(self.queue[index], end=" <-- ")
            index = (index + 1) % self.capacity
        print()

    def front_element(self):
        if self.size == 0:
            print("Queue is Empty")
            return
        print("Front Element is:", self.queue[self.front])

# Driver code to test the CircularQueue class
if __name__ == "__main__":
    q = CircularQueue(4)

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