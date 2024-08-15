## 01. Array Linear Data structure

An array is a linear data structure that stores a collection of elements, typically of the same data type, in a contiguous block of memory.

Example: 

 - List of integers

   numbers = [10, 20, 30, 40, 50]

 - List of strings

   fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

  Python does not have built-in support for Arrays, but Python Lists can be used as array.
  
  The array contains the index, memory address, and value as shown on the table. Each integer occupies 4 bytes of memory. 
  
  If we understand this, we can easily understand the 64-bit concept, which is the same; only the memory size is different. 
  
  In 32-bit systems, we require 4 bytes for each individual element.
 
 - **Index**: refers to a position or a sequential number that identifies the location of an element within a data structure. 
            
   Index is essential for accessing and manipulating specific elements in a data structure

 - **Memory Address**: refers to a unique identifier that represents the location of a value in the computer's memory.
 
 - **Value**:  refers to the actual data or content stored at a specific location in memory. [Example](https://github.com/DerartuDagne/Data-Structure-and-Algorithms/blob/main/Data%20Structures/Arrays/understanding_index%2C_memory_address%2C_value_in_array.py)
 
![image](https://github.com/user-attachments/assets/7a168360-cd23-4782-92ad-364e7847219f)

### Why Use an Array?

Simplified Management: Instead of managing multiple variables, you have a single list variable.

Scalability: Easily scale to handle hundreds or thousands of items.

Ease of Access: Access any item using its index.

Efficient Searching: Loop through the list to find specific items.

Let's take example, a list of student names. Storing each student's name in a single variable can be cumbersome and inefficient. 

Using an array (or list in Python) simplifies the management of these names.

[Example Without Array](https://github.com/DerartuDagne/Data-Structure-and-Algorithms/blob/main/Data%20Structures/Arrays/importance_of_arrays.py)

Using individual variables for each student's name:
    
    student1 = "Alice"
    
    student2 = "Bob"
    
    student3 = "Charlie"

#### What if we want to find "Bob"?
  
  if student1 == "Bob":
  
    print("Found Bob in student1")
    
  elif student2 == "Bob":
  
    print("Found Bob in student2")
    
  elif student3 == "Bob":
  
    print("Found Bob in student3")
    
  else:
  
    print("Bob not found")
    
This approach is not scalable and becomes unwieldy as the number of students increases.

[Example With Array](https://github.com/DerartuDagne/Data-Structure-and-Algorithms/blob/main/Data%20Structures/Arrays/importance_of_arrays.py)

Using an array (or list) to store and manage the student names:

Arrays allow for efficient access to elements using an index, which represents the position of the element within the array.

[Another Example with More Students](https://github.com/DerartuDagne/Data-Structure-and-Algorithms/blob/main/Data%20Structures/Arrays/importance_of_arrays.py)

Imagine we have 300 student names. Using individual variables would be impractical.

With an array, we can easily manage and search through the list.

## Types of Arrays

Arrays can generally be categorized into two main types:

***Static Array**:

A static array is an array where the size is determined and allocated at compile time. This means that the amount of memory 

required for the array is fixed and cannot be changed during program execution.

Characteristics:

- Fixed Size: The size of the array is set when the program is compiled and cannot be altered later.

- Memory Allocation: Memory for the array is allocated statically at compile time, which can lead to efficient use of resources.

- Limitations: Since the size is fixed, there can be wasted space if the array is not fully utilized, or insufficient space if the array 

grows beyond its initial size.

***Dynamic Array***:

A dynamic array is an array where the size is determined at runtime. This allows the array to grow or shrink as needed during 

the execution of the program.

Characteristics:

- Flexible Size: The size of the array can be modified during runtime, which provides greater flexibility to handle varying amounts of data.

- Memory Allocation: Memory for the array is allocated dynamically during program execution, typically using heap memory.

- Advantages: Allows for efficient memory usage as the array can expand or contract based on actual needs. This prevents the allocation of 

   excess memory and allows for handling larger datasets that are not known at compile time.

- Management: The system manages resizing and memory reallocation, which can involve overhead in terms of performance compared

  to static arrays

 Python does not have a built-in static array type like those found in languages such as C or C++. In Python, lists are the most common 
 
 data structure used to handle collections of items, and they function more like dynamic arrays rather than static arrays.

## Applications of Array
 
Arrays are used in a wide variety of applications, including:

- Storing data for processing
  
- Implementing data structures such as stacks and queues
  
- Representing data in tables and matrices
  
- Creating dynamic data structures such as linked lists and trees

 ## Common Array Method Interms of Complexity
 
  Common Array Method Interms of Complexity to identify either Worst case scenario or Average case scenario

|No.  |Methods                        |Time Complexity|
|-----|--------------------------------|--------------------------------|
|01   |       Access |O(1)|
|02   |Search      |O(n)|
|03   |Insert      |O(n)|
|04   |Delete       |beginning O(n), MiddleO(n),End O(1)|
|05   |Traversal       |O(n)| 
