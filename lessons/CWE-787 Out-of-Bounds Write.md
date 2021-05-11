## What is an Out-of-Bounds Write?

### Background
The C language has been around for decades. Since the creation of languages like it, dozens upon dozens of other languages have been made available to programmers, 
yet C is still seen in most universities and in many aspects of the industry today. 
C is still used today in software such as operating systems and embedded systems because it can perform much faster than other, higher-level alternatives that are currently available.

While having this performance is an advantage, the choice to use C for a software project comes with sacrifices in order to gain improved performance. 
The biggest sacrifice comes in the form of security. While C is considered to be the fastest high-level language, it is also one of the least secure high level languages, because it does not include any memory management out of the box. This means it is
extremely important to always think about security when writing C code, which brings us to this lesson. 

### Out-of-Bounds Writing
One of the most common security issues that comes up in C code is Out-of-Bounds Writing. 
First, let us take a look at a simple, yet very common example of an Out-of-Bounds Write.

```C
int data[4];
data[0] = 1; //valid
data[1] = 2; //valid
data[2] = 3; //valid
data[3] = 4; //valid
data[4] = 5; // NOT VALID!!!
```

Here we have a simple snippet that creates an integer array. Then the program assigns values to the indices in the array. 
Sounds simple enough, so what is the issue? The issue here is that the code is trying to assign a fifth value to the array when the array only contains 4 elements. 
Since this is the case, the program is trying to write to memory that is outside the bounds of the array. This is known as
an Out-of-Bounds Write error and is an example of what is called a segmentation fault. A segmentation fault occurs when a program tries to access
memory that it should not have permission to use. 

In most other languages today, something like this would be detected at runtime, leading to a segmentation fault runtime error, resulting in a crash. However, when it comes to C, the detection of a segmentation fault is not always guaranteed as the language does not include memory checking as part of its spec. Most causes of segmentation faults result in undefined behavior. In C, if something results in an undefined behavior, then it is "up to" the system to decide what happens. Some systems may detect the segmentation fault and terminate the program, but it is not guaranteed.

Since this is the case, we want to make sure our C code contains no segmentation faults. This means we need to prevent Out-of-Bounds Writing. 

### Why does it matter?
Why is preventing Out-of-Bounds writing so important? If the above example code were to be run and the segmentation fault was not detected, then the code would
overrite any data that is located right next to our array in memory. Overwriting data that we are not supposed to overwrite can result in many different, undesired behaviors. 
These behaviors can range from simply editing a value we did not intend to edit, to crashing the system. In the worse case, if a program has an Out-of-Bounds Write vulnerability, it could be exploited by a hacker to run unauthorized code by the program. This in turn could allow the hacker to have access to information they should not have access to, or do something even more nefarious.

### How do I prevent it?
So when it comes to writing values to elements in an array, how can we make sure that an Out-of-Bounds Write error does not occur? Before using a number as an index to write to an array element, we must make sure that number is within the bounds of our arrays length. Remember, arrays always start at index 0, so we can not accept an index that is less than 0. Since arrays start at index 0, it is also important to remember that the index of the last element in the array is always the length of the array minus 1. If we take another look at the example above, we see that the size of the array is 4, but the largest number that can be used as an index for the array is 3 (4-1). 

For more examples of this weakness and further information visit: <https://cwe.mitre.org/data/definitions/787.html>
