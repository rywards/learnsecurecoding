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
First, let's take a look at a simple, yet very common example of an Out-of-Bounds Write: 

```C

int data[4];
data[0] = 1; 
data[1] = 2; 
data[2] = 3; 
data[3] = 4; 
data[4] = 5; 



```

Here we have a simple program that creates an integer. Then the program assigns values to the indices in the array. 
Sounds simple enough, what's the issue? The issue here is that the code is trying to assign a fifth value to the array when the array only contains 4 elements. 
Since this is the case, the program is trying to write to memory that is outside the bounds of the array. This is known as
an Out-of-Bounds Write error and is an example of what is called a segmentation fault. A segmentation fault occurs when a program tries to access
memory that it doesn't have permission to use. 

In most other languages today, something like this would be detected at runtime. Then the programmer
would be met with a segmentation fault runtime error and that would be that. However, when it comes to C, the detection of a segmentation fault 
is not always guaranteed as most causes of segmentation faults result in undefined behavior. In C, if something results in an undefined behavior, 
then it is "up to" the computer to decide what happens. So depending on the computer, the segmentation fault may or may not occur. 

Since this is the case, we want to make sure our C code contains no segmentation faults. This means we need to prevent Out-of-Bounds Writing. 

Why is preventing Out-of-Bounds writing so important? If the above example code were to be run and the segmentation fault wasn't detected, then the code would
overrite any data that is located right next to our array in memory. Overwriting data that we aren't supposed to overwrite can result in many different, undesired behaviors. 
These behaviors can range from 





