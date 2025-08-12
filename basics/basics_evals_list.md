# List of Basic Evaluations

This will be a list of evaluations for the ability of AI to create and manipulate basic Python programs, involving operations, loops, functions, data types, and debugging programs involving the above. This is based on Chapters 1 through 8 of Automate the Boring Stuff with Python. While this largely replicates previous work, it seems beneficial to include this as part of the broader automation evals suite.

## Section 1: Variables, Data Types, and Conditionals

(based on chapters 1 and 2 of Automate the Boring Stuff)

1. Write a Python program that has one function, spam_greeter, that takes in one argument called spam, returns 'Hello' if 1 is stored in spam, 'Howdy' if 2 is stored in spam, and 'Greetings!' if anything else is stored in spam.
2. Write a Python program that has one function, opposite_day, that takes in a single Boolean argument that denotes whether it is Opposite Day or not. Define a variable within the function that determines whether to say it is Opposite Day or not. Have that be the input if it is not Opposite Day, and have it be the inverse of the input if it is Opposite Day. If that internal variable is true, return 'Today is Opposite Day.' If not, return 'Today is not Opposite Day.'
3. Write a Python program that computes the discrepancy between advertised and actual storage capacities for computer storage devices. It takes in two arguments: unit and ad_capacity. Unit can be kb, mb, gb, or tb, all as strings. If kb, multiply ad_capabity by 10^3/2^10, if mb, multiply by 10^6/2^20, and so on. Return the actual capacity as computed here.

## Section 2: Loops, Functions, and Debugging

(based on Chapters 3, 4, and 5 of Automate the Boring Stuff)

4. Write a Python program that uses a for loop to print the numbers 1 to 10.
5. Write a Python program that uses a while loop to print the numbers 1 to 10.
6. Write a Python program that has one function, collatz, that takes in an integer and prints the Collatz sequence starting at that integer until it reaches 1.
7. Write a Python program that has one function, collatz, that takes in an integer and prints the Collatz sequence starting at that integer until it reaches 1. If the input is a float, string, etc., handle conversion to an integer, rounding down if necessary.
8. Write a Python program that has one function, collatz, that takes in an integer and prints the Collatz sequence starting at that integer until it reaches 1. If the input is a float, string, etc., handle conversion to an integer (if it can be converted), rounding down if necessary. However, if the input is the string "squirrel," raise a SquirrelError with the error message "Squirrels can't go out in the hail!"
9. Write a function that takes in two variables, x and y. It should return the string "I love to eat x and y" with those variables substituted into that line. However, if the strings are the same as each other, even if their cases are different, (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'), use an assert statement to trigger an AssertionError.

## Section 3: Hashable Data Types

(based on Chapters 6, 7, and 8 of Automate the Boring Stuff)

10. 