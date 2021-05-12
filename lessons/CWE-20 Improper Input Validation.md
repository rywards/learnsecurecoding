## What is Improper Input Validation?

### Background
When a program takes input from a user, there is never a guarantee that they will provide the type of input that it is expecting. As a simple example, imagine you are writing a function called ‘ageDoubled’ that can take in an age and multiply it by two. If you simply parse an integer from their input, then if they type something like "Z" or "Two", the code will fail to parse an integer. If it does not crash, then it will again cause an error when it attempts to multiply "Z" by 2.

### Input Validation
The act of _validating_ a user's _input_, to make sure it is something that is expected and can be dealt with, is called input validation. Input validation in the previous example can be done different ways. One way is to write a complex function that can handle multiple data types and data in different formats (Like typing out nineteen vs 19). The other way to validate your inputs is by limiting what the user is able to input.

## Why Does It Matter? 
Failing to properly validate user input can result in users inputting things the code cannot handle, leading to errors, incorrect results, or crashes. As mentioned above, inputting a string when a function is written to handle only integers could cause your code to throw an error. Another example might be someone typing out a phone number word by word as opposed to numerically or using HTML tags in their written response. Not all users will play by the rules, and some may even be malicious. Never underestimate users’ impressive ability to find unconventional ways to input data that you did not foresee. And most important of all, **Never Trust the User.**

If strings are not properly validated, it can be possible for users to input malicious code into your program. One common example is SQL injection. If SQL queries are not properly prepared and data is not properly validated, a user can do some very bad things to the database. **Never Trust the User.**

![test](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

## How Can You Prevent These Issues? 
Once again: **Never Trust the User.** There are many different tactics that can be taken to help prevent unvalidated data into your program. The first thing that you want to do is keep track of any place where it is possible for the user to input information. From there you can make sure that each of these areas has protections and validators in place. 

One option for input validation is to add limitations to the input box in order to prevent improper data types from being inputted. A common example of this is only allowing numbers to be typed in a phone number field. A second method that is often used is only accepting inputs that have been whitelisted. This can be done by implementing a drop-down menu for users to select values from predetermined list so that you can be certain your code is able to handle the selection. And the third, most important method is to reject any input that is not expected. You shouldn't just use one method for input validation. Each is a line of defense, and no one line of defense is 100% perfect.

If you are accepting text from a user, you also might want to implement regex statements that prevent the execution of code that calls functions in your own code. This would prevent issues stemming from people having knowledge of your source code and prevents users from calling functions they are not supposed to have access to.

When confirming that you are validating your user inputs it is easy to focus on places where the user is directly able to type information into a box and send it to the server, but there are other ways for users to send back data that programmers should be aware of. One of the most commonly missed of these is the ability to edit cookies through third party programs allowing the programmer to inject data that the programmer did not validate. Fixing issues that stem from these kinds of exploits take much more effort and often require making decisions to prevent them during the planning and initial design of the project.

Overall Improper Input Validation is something that all coders should be aware of and keeping an eye out for whenever they are taking data into a program.

For more examples of this weakness and further information visit: <https://cwe.mitre.org/data/definitions/20.html>
