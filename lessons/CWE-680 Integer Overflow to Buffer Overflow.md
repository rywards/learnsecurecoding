**Lesson Outline**

This lesson builds upon the concepts for two seperate CWE's. CWE-190: Integer overflow or wraparound, which has already been covered in this unit and CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer (informally called buffer overflow). This lesson will provide some information on what a buffer overflow is, and outline some of the causes and effects of an integer overflow to bufffer overflow.

**What is a Buffer Overflow**

This section will briefly cover what a memory buffer overflow is, however it will not be a comprehensive lesson. More information regarding CWE-119 can be found at https://cwe.mitre.org/data/definitions/119.html. 

A memory buffer overflow refers to a vulnerability that takes advantage of of a program that performs operations on a memory buffer. If the bounds of the buffer are not checked or enforced the program could accidentally read from or write to a memory location outside the intended boundary for that buffer. Because of this an attacker may be able to execute arbitrary code, alter the intended flow control, read sensitive information, or cause the system to crash. Any of these outcomes are unattractive to developers. 

**How does an Integer Overflow lead to a Buffer Overflow**

If the programs position in the memory buffer is determined by an integer, and the bounds of that integer are not checked, this could mean an integer overflow would cascade into a buffer overflow. For example, lets say you are iterating through a portion of a memory buffer using a for loop with a counter. Lets also say that counter is an integer named i. If the bounds of i are not checked, this could lead to the program writing outside the intended portion of a memory buffer, should i unexpectedly overflow or wraparound. Should this happen it can lead to any of the potential outcomes outlined above for buffer overflow.
