
# ![image](https://github.com/user-attachments/assets/73495fde-97db-4ecb-8514-65ba3a520b42) Notation


Big O is a method for evaluating the efficiency of an algorithm. It describes the performance or complexity of an algorithm, allowing for comparison of the efficiency of different algorithms. Big O notation is an essential tool for computer scientists, Machine Learning Engineer, Data Engineer, Full stack developer and Software Engineer to assess and compare the time and space complexity of algorithms.


## Why we need BIG O ?

Big O notation is crucial for assessing, selecting, and predicting the performance of algorithms, offering a standardized and theoretical framework that is essential in computer science, software engineering and others.

**Why Use Big O Notation Instead of Actual Execution Time?**
  
Hardware Independence:

Actual execution time can vary based on hardware factors like processor speed and memory. We cannot depend on our system clock because every time we run our program, it relies on the system's current state and performance. Big O notation abstracts these details, providing a hardware-independent way to analyze and compare algorithm efficiency.


## Practical Uses of Big O Notation

As the amount of data increases, the time it takes for an algorithm to run can become unmanageable, even for tasks that initially seem straightforward. Knowing an algorithm's time complexity helps developers choose the best approach for different situations and refine their code to enhance efficiency.

Big O notation plays a crucial role in various real-world applications, helping developers and computer scientists optimize and evaluate the performance of algorithms in different scenarios. Here are some key applications:

**1.Algorithm Optimization**

Sorting and Searching: 
Big O notation helps in choosing the most efficient sorting or searching algorithm for a given dataset.
Data Processing: When processing large amounts of data, understanding the time complexity helps in selecting algorithms that can handle the data efficiently without causing performance bottlenecks.

**2.System Design**

Scalability: Utilized to ensure that algorithms and data structures scale effectively with increasing data sizes or user loads, influencing choices like caching mechanisms or database indexing strategies.
Resource Management: Assists in designing systems that efficiently manage resources like memory and CPU time, ensuring optimal performance under varying conditions.

**3.Software Development**

Performance Tuning: Developers leverage Big O notation to identify and optimize performance-critical code sections, ensuring applications run smoothly and efficiently.
Code Reviews: During code reviews, Big O notation is used to evaluate the potential performance impacts of new algorithms or data structures.

**4.Competitive Programming**

Problem Solving: Competitive programmers use Big O notation to develop algorithms that solve problems within given time constraints, often striving for the best possible complexity.
Benchmarking: Facilitates the comparison of different solutions to the same problem, ensuring the selection of the most efficient algorithm for implementation.

**5.Machine Learning and Data Science**

Model Training: Helps in understanding and optimizing the training time of machine learning models, particularly with large datasets and complex algorithms.
Data Analysis: In data science, efficient algorithms are crucial for processing and analyzing large datasets, making Big O notation 
essential for selecting appropriate techniques.

**6.Network Design**

Routing Algorithms: In networking, Big O notation aids in evaluating the efficiency of routing algorithms, ensuring data packets are delivered efficiently across the network.
Load Balancing: Assists in designing load balancing algorithms that distribute traffic evenly across servers, minimizing response times and maximizing throughput.

## Types of Big O Notations

![image](https://github.com/DerartuDagne/Data-Structure-and-Algorithms/assets/112087783/2f848fa4-bac3-421a-a5c3-b4042692c965)

 Complexity chart for all big O notations. | Image: WIkimedia Commons
|No.  |Complexity Name                     |Rank|
|-----|--------------------------------|---------------------|
|01   |[O(1): Constant complexity](https://github.com/DerartuDagne/Data-Structure-and-Algorithms/blob/main/BIG%20O/o(1)_constant_complexity.py)|Excellent/Best|
|02   |[O(logn): Logarithmic complexity](https://github.com/DerartuDagne/Data-Structure-and-Algorithms/blob/main/BIG%20O/o(logn)_logarithmic_complexity.py) |Good|
|03   |[ O(n): Linear complexity]()        |Fair|
|04   |[O(nlogn): Loglinear complexity]()         |Bad|
|05   |[O(n^x): Polynomial complexity]()         |Horiible|
|06   |[O(X^n): Exponential time]()         |Horrible|
|07   |[O(n!): Factorial complexity]()        |Horrible|


1.[O(1): Constant complexity](https://github.com/DerartuDagne/Data-Structure-and-Algorithms/blob/main/BIG%20O/o(1)_constant_complexity.py).

   Constant time algorithms always take the same amount of time to execute, regardless of the input size. The algorithm's running time is 
   
   independent of the input size, making it more efficient than others, as we can see above. A good example of O(1) time complexity is 
   
   accessing a value in an array using an index.
   
2.[O(logn): Logarithmic complexity](https://github.com/DerartuDagne/Data-Structure-and-Algorithms/blob/main/BIG%20O/o(logn)_logarithmic_complexity.py).
    
    Let's start with the definition of logarithm to get the concept of it.

    "A logarithm is the power to which a base, usually 10 or e (Euler's number), must be raised to produce a 
     given number. "
    
     In mathematical terms, if b^y = x, then y is the logarithm of x to the base b, written as logb(x)=y.

     Example:

     If 2^10 = 1024,then the logarithm of 1024 to the base 2 is 10, then the logarithm of 1024 to the base 2 
     is 10, written as log2(1024) = 10.
    
   * Desirable Efficiency: Functions with O(logN) complexity are very efficient, close to O(1) functions.
   * Common Use: Many algorithms have 𝑂(log𝑁)complexity, making it important to recognize and understand.

     **Examples of 𝑂(log𝑁) Complexity**
   
   * Binary Search: Finding an element in a sorted array.
     
       Instead of iterating through an entire array to find a value, a binary search offers a more efficient
       method. Here’s how it works:
     
       Initialize: Set min = 0 and max = n - 1.
     
       Calculate Midpoint: Find the middle index: mid = (min + max) // 2.
     
       Compare:
     
              If arr[mid] == target, return mid.
     
              If arr[mid] < target, set min = mid + 1.
     
              Otherwise, set max = mid - 1.
     
        Repeat: Go back to step 2 until the target is found or the range is empty.
     
     **Example in Action**
     
     Let's find the value 46 in the array [4, 8, 10, 14, 27, 31, 42, 52]:

             Initial Setup: min = 0, max = 7

     **First Iteration:**
     
              mid = (0 + 7) // 2 = 3

               arr[3] = 14 (less than 46), so set min = 4
     
     **Second Iteration:**
     
                mid = (4 + 7) // 2 = 5
     
                arr[5] = 31 (less than 46), so set min = 6
     
     
     **Third Iteration:**
     
                 mid = (6 + 7) // 2 = 6
     
                 arr[6] = 42 (equals target), return 6
     
     
     ### Understanding 𝑂(log𝑁) Complexity

     
     Binary search reduces the search area by half each iteration:

                   Initial Array: N = 8

                   First Step: N = 4

                   Second Step: N = 2

                   Third Step: N = 1

     N = 8, [4, 8, 10, 14, 27, 31, 42, 52] //Compared and divide search area by 2
     
     N = 4, [27, 31, 42, 52] //Compared and divide search area by 2
     
     N = 2, [42, 52] //Compared mid to target. They matched, so returned mid.

   Notice that this took three steps and it's dividing by 2 each time. 
   
   If we multiplied by 2 each time we would have 2 x 2 x 2 = 8, or 2^3 =  8.

                 2^3 = 8 -> log2 ^8 = 3
    
                 2k = N -> log2 N = k

 4. O(n): Linear complexity.
 5. O(nlogn): Loglinear complexity.
 6. O(n^x): Polynomial complexity.
 7. O(X^n): Exponential time.
 8. O(n!): Factorial complexity.
