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

# Array Methods

   |No.  |Data structure           | Categories|
   |-----|--------------------------------|---------------------|
   |01   |append()|Adds an element at the end of the array list|
   |02   |reverse()|Reverses the order of an array list|
   |03   |clear()|Eliminates all elements from the array list|
   |04   |pop()|Removes an element from the specified position|
   |04   |count()|Returns the elements along with their total number|
   |05   |insert()|Adds an element to the specified position in the array list|
   |06   |copy()|Returns a copy of the array list|
   |07   |extend()|Add the elements of an array list to the end of the current list|
   |08   |remove()|Eliminates the first element with the specified value|
   |09   | index()|Returns the index of the first element in an array list with the specified value|
   |10   | sort()|Sorts the array list|
