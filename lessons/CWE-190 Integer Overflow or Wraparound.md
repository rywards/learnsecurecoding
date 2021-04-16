Most coders learn about primitive data types early into their careers. The most common primitive data type is the integer, which stores its value in a fixed number of bits.

The value an integer can store is dependent on the number of bits it contains, and whether it is signed or unsigned. For signed integers, the leftmost bit (also known as the Most Significant Bit, the MSB) determines whether the number is positive or negative. `0` represents a positive number, and `1` represents a negative.

Some programmers may be familiar with how to count in binary. Below is an example of all possible values a 3-bit unsigned integer can have.

```verilog
000 = 0
001 = 1
010 = 2
011 = 3
100 = 4
101 = 5
110 = 6
111 = 7
```

When computers count in binary, they follow a simple pattern. The least significant bit (LSB) flips from 1 to 0 and back every number, and subsequent bits only flip if all bits to the right are 1. So what will a computer do after all bits are 1? It flips to all zeros.

```verilog
110 = 6
111 = 7
000 = 0
001 = 1
```

This is known as an _integer overflow_. When an integer is incremented greater than its maximum value, it "wraps around" to its minimum possible value.

This also occurs for signed integers. If a programmer is not careful to make sure their 


Need To Rewrite: Early in most coders careers they are taught about the primitive data types of the language that they are using. This often includes characters, Strings, and Integers. On top of those many popular languages like Java include the Long which function similarly to Integers but can be twice as long.  
 
When a value in a program in incremented or changed to a value too large for the current index that is known as an Integer Overflow or Wraparound. While coders can write code that intentionally wraps around, in situations where it was not planned it can cause the values being returned to be extremely small number or negative depending on the language and the implementation. 
This kind of weakness is almost always introduced during the implementation phase.

This type of error can lead to many other problems and often is responsible for undefined behavior and lead to crashes. On top of this it can lead to infinite loops if the loop indexer code is written in a way that contains this weakness. If the error occurs when adding value or less specifically, when it is effects code that is ‘Data’ it can cause incorrect calculations and outputs down the line. 

The is an Apocryphal story about the coding of Civilization 2 that attributes the character Gandhi’s aggression in the title to an overflow error. The story goes that there was a ‘Friendship’ attribute for each character and that to match his demeanor they set this value to the maximum to ensure he would be the most forgiving of the characters. This worked well until the Player did anything to Gandhi that caused him to like them more, this would cause the ‘Friendship’ attribute to increment but due to the fact that it was already at its highest value it instead looped to the bottom of the available values. This caused Gandhi to almost always be incredibly aggressive despite the coder’s original intentions. While this story was later disproven by analysis of the code it is a good example of how Integer overflows can cause errors and unexpected behavior in your code.
