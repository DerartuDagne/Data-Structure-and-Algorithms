# Data Structure

Data Structures are mechanisms designed to store and organize data in memory, allowing for efficient access and modification. 

The name "data structure" itself indicates the purpose of organizing data in memory.  There are many ways to structure data in memory, 

each tailored to specific needs for efficient data handling and operations. 

Data structures can be classified into different types. Each type serves specific purposes and offers unique advantages for various applications.

Let’s look at the following code:
  
    greeting = "Good morning, "
   
    name = "Alice. "
   
    question = "How was your night?"
   
    message = greeting + name + question
   
    print (message)

This simple program handles three pieces of data, combining them to form one coherent message. If we describe the data organization in this program,

we see three independent strings, each stored in a separate variable.

However, we can also store this data in an array:

      array = ["Good morning","Alice! ", "How was your night? "]

      print array[0] + array[1] + array[2]
   
The organization of our data can greatly influence the speed of our program, potentially making it run significantly faster or slower. 

Choosing the right data structures is essential for optimizing performance and ensuring that programs can handle large amounts of data efficiently.

   ## Types of Data structure

  ### Primitive Data structue
      
   Primitive data structures are the fundamental data types that serve as the basic building blocks for data manipulation. 

   These are the simplest forms of data structures, directly supported by the hardware and typically provided by the programming language.

   These primitive data structures are built into the language and supported by the system's hardware, making them very efficient and easy to use. 

   They serve as the foundation for creating more complex data structures.

   Here are the common primitive data structures: Integers, Float, Strings, Boolean

   ### NonPrimitive Data structure

   Non-primitive data structures are more complex data structures that are composed of primitive data types and provide more flexibility in organizing and storing data.

   Unlike primitive data types, which are directly supported by the programming language and typically have fixed sizes and operations, non-primitive data structures are user-defined and can vary in size and complexity.

   They are implemented using primitive data types and are designed to efficiently manage large amounts of data.

   NonPrimitive Data structure are classified into two these are: Linear Data structures and Non Linear Data structure
      

   |No.  |Data structure           | Categories|
   |-----|--------------------------------|---------------------|
   |01   |[Array]()|Linear Data structure | 
   |02   |[Stack]() |Linear Data structure |
   |03   |[Queue]() |Linear Data structure |
   |04   |[Linked List]() |Linear Data structure |
   |05   |[Tree]() |NonLinear Data structure |
   |06   |[Graph]() |NonLinear Data structure |
   |07   |[Hash Table]() |NonLinear Data structure |
   |08   |[Binary search]() |NonLinear Data structure |
   |09   |[tuples]() |Python Data structure |
   |10   |[dictionary]() |Python Data structure |
   |11   |[Set]() |Python Data structure |
   |12   |[list]() |Python Data structure |

   #### 01. [Array Linear Data structure]()
