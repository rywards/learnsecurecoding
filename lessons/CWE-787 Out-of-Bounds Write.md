The C language has been around for decades. Since the creation of these 
languages, dozens upon dozens of other languages have been made available to programmers, 
yet C is still seen in most Universities and in some aspects of the Industry today. 
C is still used today in software such as Operating and Embedded Systems because it so 
much faster than any other higher level language we have today. 

While having this incredibe speed is fantastic, C makes sacrifices in order to obtain this
speed. The biggest sacrifice comes in the form of security. While C is the fastest high
level language, it is also one of the least secure high level languages. This means it is
extremely important to always think about security when writing C code, which brings us to this lesson. 

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

Here we have a simple program that creates an integer array. Then the program assigns values to the indices in the array. 
Sounds simple enough, so what is the issue? The issue here is that the code is trying to assign a fifth value to the array when the array only contains 4 elements. 
Since this is the case, the program is trying to write to memory that is outside the bounds of the array. This is known as
an Out-of-Bounds Write error and is an example of what is called a segmentation fault. A segmentation fault occurs when a program tries to access
memory that it does not have permission to use. 

In most other languages today, something like this would be detected at runtime. Then the programmer
would be met with a segmentation fault runtime error and that would be that. However, when it comes to C, the detection of a segmentation fault 
is not always guaranteed as most causes of segmentation faults result in undefined behavior. In C, if something results in an undefined behavior, 
then it is "up to" the computer to decide what happens. So depending on the computer, the segmentation fault may or may not occur. 

Since this is the case, we want to make sure our C code contains no segmentation faults. This means we need to prevent Out-of-Bounds Writing. 

Why is preventing Out-of-Bounds writing so important? If the above example code were to be run and the segmentation fault was not detected, then the code would
overrite any data that is located right next to our array in memory. Overwriting data that we are not supposed to overwrite can result in many different, undesired behaviors. 
These behaviors can range from simply editing a value we did not intend to edit, to crashing our computer. In the worse case, if by some chance a hacker were to see that our program had Out-of-Bounds Writing issues, the hacker could try to exploit that security issue. An example of this could
be that the hacker uses this exploit to run unauthorized code in our program. This in turn could allow the hacker to have access to information they should not have access to. 

So when it comes to writing values to elements in an array, how can we make sure that an Out-of-Bounds Write error does not occur? Before using a number as an index to write to an array element, we must make sure that number is within the bounds of our arrays length. Remember, arrays always start at index 0, so we can notaccept an index that is less than 0. Since arrays start at index 0, it is also important to remember that the index of the last element in the array is always the length of the array - 1. If we take another look at the example above, we see that the size of the array is 4, but the largest number that can be used as an index for the array is 3 (4-1). 

We hope you found this informative!



For more examples of this weakness and further information visit: <https://cwe.mitre.org/data/definitions/787.html>


