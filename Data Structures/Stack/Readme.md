# What is Stack Linear Data Structure?


A stack is a linear data structure  that operates on a Last-In-First-Out (LIFO) basis. Real-life examples of a stack are a deck of cards, piles of books, piles of money, and many more.


  <p align="center">
  <img src="https://github.com/user-attachments/assets/5fa97e1a-ae68-4f64-acb5-26043ae23260" alt="Stack of Books" width="400" />
</p>

## LIFO(Last In First Out) Principle in Stack Data Structure:

- Inserted last will come out first.
  
 ![image](https://github.com/user-attachments/assets/030c0b68-62d8-4aad-8b91-be6261046439)Source: Simple learn.com
 
 ## Exploring Stack Data Structures and Their Methods

- Push: Adds an element to the top of the stack.

- Pop: Removes the top element from the stack.

- Peek: Returns the top element without removing it.

- IsEmpty: Checks if the stack is empty.

- IsFull: Checks if the stack is full (in case of fixed-size arrays)Understanding Stack Data Structures
 
Imagine we have a stack of books arranged on a table. This stack represents a stack data structure, where we can only interact
 
 with the book at the very top.

- Viewing the Top Book: We can only see and access the top-most book. For example, the book numbered 40 is currently on the top of the stack.

- Adding a New Book: If we want to place a new book, say 50, we need to place it on top of the stack.
  
  This means that book 50 will now be the top-most book, and book 40 will move below it.

- Accessing a Different Book: If we want to access a book that is not on the top, like book 40, we must first remove the top book.

   Once book 50 is removed, book 40 becomes the new top of the stack, and we can now see and access it.

This principle illustrates the Last In, First Out (LIFO) nature of stacks, where the last item added is the first one to be removed.

 ![image](https://github.com/user-attachments/assets/660a6207-ac28-4142-81e8-637c1d5c7d9e)                  
                                                                   Source: Simple learn.com


## Types of Stack Data Structures

-  ***Fixed-Size Stack***: This stack has a predetermined size that remains constant. It cannot adjust its size to accommodate more elements

   or reduce its size. If you try to push an element onto a full stack, it results in an overflow error. Conversely, if you attempt to pop 

   an element from an empty stack, it triggers an underflow error.

- ***Dynamic-Size Stack***: Unlike the fixed-size stack, a dynamic-size stack can expand or contract as needed.

   It automatically increases its capacity when it becomes full and decreases its size when it becomes empty. This flexibility is typically 
 
   achieved using a linked list, which supports easy resizing and efficient management of the stack’s size.

## Applications of Stack Data Structures

- Recursion

- Expression Evaluation and Parsing

- Depth-First Search (DFS)
  
- Undo/Redo Operations
  
- Browser History
  
- Function Calls



