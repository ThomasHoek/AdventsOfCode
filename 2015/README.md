# Advents of Code tips for 2015

These are little tips and tricks I used to solve the puzzles

## day 1

day 1 honestly is not hard, just a counter or for loop will suffice.

## day 2

day 2 requires just some control over the variables. Try to split it up to a length, width and height variable.

## day 3

I personally used tuple magic here with (loc_x, loc_y).
Might be easier to use solve using string matching if statements

## day 4

Most programming languages have libraries for solving md5.
if not good luck...
C and C++ can use custom created files from github. Don't program md5 yourself.

## day 5

I used a few seperate functions for checking vowels, doubles and strings.
Then a counter if all three returned True.

## day 6

I used an 1000, 1000 matrix array and created a function to iterate over the matrix and swap boolians/ integers. Probably can be solved smart by overwriting entire entire slices at once. At the end I used a sum.

## day 7

I used 50 if statements... kind of a bad solution but it works.
I iterated infinitely over every puzzle input, and removed the one's that were solved. The last one to be solved was "a".
This is a bad way since I iterate many times over the same value.

Better solution would be a dictionary or mapping of letter to their command, keep track in a list which letters got solved and which new letters are added.
When a letter is solved remove it from the list. Then solve until A is found.

## day 8

I used a pointer which searched for the first occurance of "\\".
Then I checked for \\x, \\\\, \\\" .
If any were found replace it with a substring of the escape being removed.
If all these were not found I would go to the next index. 
When a sentence is done, sum and add it to a counter.

second part was way easier to solve, just count amount of \\\\ or \\"

## day 9

I brute forced every possible permutation. Not a good solution but solved it.

## day 10



## day 11

## day 12

## day 13

## day 14

## day 15

## day 16

## day 17

## day 18

## day 19

## day 20

## day 21

## day 22

## day 23

## day 24

## day 25
