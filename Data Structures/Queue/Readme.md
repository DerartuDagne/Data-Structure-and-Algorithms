# What is Queue Linear Data Structure?

A queue is a linear data structure that operates on the First-In-First-Out (FIFO) principle. 

It behaves like a queue of people: new elements are appended at the rear, while elements are removed from the front. The person who comes 

first will be served first. This ensures that the earliest added element is the first one to be removed.

![image](https://github.com/user-attachments/assets/a60f4485-d58b-43c5-989e-8a05d1d3132d)

# Methods of Queue Data Structure

- Enqueue (Insert): Adds an element to the rear of the queue.
  
- Dequeue (Delete): Removes and returns the element from the front of the queue.
  
- Peek: Returns the element at the front of the queue without removing it.
  
- Empty: Checks if the queue is empty.
  
- Full: Checks if the queue is full.

## Differences of Stack and Queue 

|Parameters |Stack                    |Queue|
|-----|--------------------------------|-----|
|Working Principle|It follows the LIFO (Last In First Out) order to store the elements,which means the element that is inserted last will come out first.|It follows the FIFO (First In First Out) order to store the elements, which means the element that is inserted first will come out first.|
|    Pointers |  It has only one end, known as the top, at which both insertion and deletion take place.                                   | It has two ends, known as the rear and front, which are used for insertion and deletion. The rear end is used to insert the elements, whereas the front end is used to delete the elements from the queue.     |
|   Operations  |   The insertion operation is known as push and the deletion operation is known as pop.                                  |The insertion operation is known as enqueue and the deletion operation is known as dequeue.      |
|   Empty Condition  |  The condition for checking if the stack is full is top==max-1 as max refers to the maximum number of elements that can be in the stack.                                   | The condition for checking if the queue is full is rear==max-1 as max refers to the maximum number of elements that can be in the queue.     |
|    Variants |     There are no other variants or types of the stack.                                |   There are three types of queues known as circular, double-ended, and priority.   |
|  Implementation   | It has a simple implementation compared to queues as no two pointers are involved.                                    |   It has a complex implementation compared to stacks as two pointers front and rear are involved.   |
|   Application  | It is used to solve recursion-based problems.                                    | It is used to solve sequential processing-based problems.     |
|  Data Representation   |  Often implemented with arrays or linked lists.                                   |  Can also be implemented with arrays or doubly linked lists.    |
|   Example  |  A real-life example of a stack can be the Undo/Redo operation in Word or Excel.                                   | A real-life example of a queue can be an operating system process scheduling queues.     |

## Applications of Queue

- Task scheduling in operating systems
  
- Data transfer in network communication
  
- Simulation of real-world systems (e.g., waiting lines)
  
- Priority queues for event processing queues for event processing
