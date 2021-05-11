## What is an Integer Overflow?

### Background

Most coders learn about primitive data types early into their careers. The most common primitive data type is the integer, which stores its value in a fixed number of bits.

The value an integer can store is dependent on the number of bits it contains, and whether it is signed or unsigned. For signed integers, the leftmost bit (also known as the Most Significant Bit, the MSB) determines whether the number is positive or negative. `0` represents a positive number, and `1` represents a negative.

Some programmers may be familiar with how to count in binary. Below is an example of all possible values a 3-bit unsigned integer can have, by counting up from 0 to 7.

```java
000 = 0
001 = 1
010 = 2
011 = 3
100 = 4
101 = 5
110 = 6
111 = 7
```

### Overflows

When computers count in binary, they follow a simple pattern. The least significant bit (LSB) flips from 1 to 0 and back every number, and subsequent bits only flip if all bits to the right are 1. So what will a computer do after all bits are 1? It flips to all zeros.

```java
110 = 6
111 = 7
000 = 0
001 = 1
```

This is known as an _integer overflow_, also known as a _wraparound_. When an integer is incremented greater than its maximum value, it "wraps around" to its minimum possible value. Likewise, if an integer is decremented to less than its minimum value, it wraps back to its maximum possible value. 

This also occurs for signed integers. If a programmer is not careful to make sure their integers do not go past their maximum/minimum values, they [may suddenly find that their train ride has nine quintillion stops remaining](https://youtu.be/48QQXpbTlVM).

A similar event occurs with signed integers. Note in the following example, with a 4-bit signed integer, that the computer follows the aforementioned simple pattern as it counts up, causing the integer\'s value to wrap back to its minimum value.

```java
0101 =  5
0110 =  6
0111 =  7
1000 = -8
1001 = -7
1010 = -6
1011 = -5
```

## Why does it matter?

This type of error can lead to many unexpected problems, and is often responsible for undefined behavior or lead to crashes. On top of this, it can lead to infinite loops if there is an overflow in the loop indexer. Additionally, if the error occurs when manipulating data, it can cause incorrect calculations.

There is an apocryphal story about the coding of Civilization 2 that attributes the character Gandhi’s aggression in the title to an overflow error. The story goes that there was a ‘Friendship’ attribute for each character and that to match his demeanor they set this value to the maximum to ensure he would be the most forgiving of the characters. This worked well until the Player did anything to Gandhi that caused him to like them more, this would cause the ‘Friendship’ attribute to increment but due to the fact that it was already at its highest value it instead looped to the bottom of the available values. This caused Gandhi to almost always be incredibly aggressive despite the coder’s original intentions. While this story was later disproven by analysis of the code it is a good example of how Integer overflows can cause errors and unexpected behavior in your code.

## How do I prevent it?

While there is not one definitive way to prevent integer overflows and wraparounds, it is not too complex to spot and fix them, as long as you are careful to watch out for it. When writing your code, take into consideration how big your integers can get. Be mindful of the range of values that the datatypes can have. For example, if your `int`s can have values in the billions, consider using a `long` instead, as the maximum value of a signed `int` is 2.147 billion. If your numbers approach the limit of a `long`, and precision is not an issue, consider using floating point numbers instead.


For more examples of this weakness and further information visit: <https://cwe.mitre.org/data/definitions/190.html>
