# List of Basic Evaluations

This will be a list of evaluations for the ability of AI to create and manipulate basic Python programs, involving operations, loops, functions, data types, and debugging programs involving the above. This is based on Chapters 1 through 8 of Automate the Boring Stuff with Python. While this largely replicates previous work, it seems beneficial to include this as part of the broader automation evals suite.

## Section 1: Variables, Data Types, and Conditionals

(based on chapters 1 and 2 of Automate the Boring Stuff)

1. Write a Python program that has one function, spam_greeter, that takes in one argument called spam, returns 'Hello' if 1 is stored in spam, 'Howdy' if 2 is stored in spam, and 'Greetings!' if anything else is stored in spam.
2. Write a Python program that has one function, opposite_day, that takes in a single Boolean argument that denotes whether it is Opposite Day or not. Define a variable within the function that determines whether to say it is Opposite Day or not. Have that be the input if it is not Opposite Day, and have it be the inverse of the input if it is Opposite Day. If that internal variable is true, return 'Today is Opposite Day.' If not, return 'Today is not Opposite Day.'
3. Write a Python program has one function, storage, that computes the discrepancy between advertised and actual storage capacities for computer storage devices. It takes in two arguments: unit and ad_capacity. Unit can be kb, mb, gb, or tb, all as strings. If kb, multiply ad_capabity by 10^3/2^10, if mb, multiply by 10^6/2^20, and so on. Return the actual capacity as computed here.

## Section 2: Loops, Functions, and Debugging

(based on Chapters 3, 4, and 5 of Automate the Boring Stuff)

4. Write a program that has a function called factorial() that computes the factorial of any integer.
5. Write a Python program that one function called to_ten() which takes no arguments and uses a for loop to print the numbers 1 to 10.
6. Write a Python program that one function called to_ten() which takes no arguments and uses a while loop to print the numbers 1 to 10.
7. Write a Python program that has one function, collatz, that takes in a positive integer as its argument and prints the Collatz sequence starting at that integer until it reaches 1.
8. Write a Python program that has one function, collatz, that takes in a positive integer as its argument and prints the Collatz sequence starting at that integer until it reaches 1. If the input is a float, string, etc., handle conversion to an integer, rounding down if necessary.
9. Write a Python program that has one function, collatz, that takes in a positive integer as its argument and prints the Collatz sequence starting at that integer until it reaches 1. If the input is a float, string, etc., handle conversion to an integer (if it can be converted), rounding down if necessary. However, if the input is the string "squirrel," raise a TypeError with the error message "Squirrels can't go out in the hail!"
10. Write a Python function named love_to_eat() that takes in two variables, x and y. It should return the string "I love to eat x and y" with those variables substituted into that line. However, if the strings are the same as each other, even if their cases are different, (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'), use an assert statement to trigger an AssertionError.

## Section 3: Hashable Data Types

(based on Chapters 6, 7, and 8 of Automate the Boring Stuff)

11. Write a Python function named list_format() that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with 'and' inserted before the last item. For example, passing the list 

spam = ['apples', 'bananas', 'tofu', 'cats']

to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to handle the case where an empty list [] is passed to your function.

12. The following data structure is in use for chessboards: a Python dictionary with keys being strings representing squares, in algebraic chess notation, and the values being two-letter strings representing pieces, where the first letter is a lowercase 'w' or 'b' to indicate the white or black color, and the second letter is an uppercase 'P', 'N', 'B', 'R', 'Q', or 'K' to represent the kind of piece. Note that not all squares are included as keys, and the absence of a key represents an empty square.

Write a Python function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on whether the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can have at most 16 pieces, of which only eight can be pawns, and all pieces must be on a valid square from '1a' to '8h'. That is, a piece can’t be on square '9z'. The piece names should begin with either a 'w' or a 'b' to represent white or black, followed by 'P', 'N', 'B', 'R', 'Q', or 'K'. This function should detect when a bug has resulted in an improper chessboard. (This isn’t an exhaustive list of requirements, but it is close enough for this exercise.)

13. Say you’re creating a medieval fantasy video game. The data structure to model the player’s inventory is a dictionary whose keys are strings describing the item in the inventory and whose values are integers detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has one rope, six torches, 42 gold coins, and so on.

Write a Python function named display_inventory() that would take any possible “inventory” and use print statements to print it like the following:

Inventory:
42 gold coin
12 arrow
6 torch
1 dagger
1 rope
Total number of items: 62

Items should first be ordered by quantity, and then alphabetically based on the keys.

14. Write a Python function named bullet() that takes in a long multi-line string and adds a bullet point, in the form of a star followed by a space, at the start of each line.

15. Write a Python function named pig_latin() that converts an input string to pig Latin. The specific rules of pig Latin we use here are as follows: If a word begins with a vowel, the word yay is added to the end of it. If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or consonant cluster is moved to the end of the word and followed by ay.

16. Write a Python function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right- justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
