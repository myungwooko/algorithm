"""
195. Tenth Line
Eas

Given a text file file.txt, print just the 10th line of the file.

Example:

Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:

Line 10
Note:
1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.



**********
unix awk*
**********
AWK command in Unix/Linux with examples
Awk is a scripting language used for manipulating data and generating reports.The awk command programming language requires 
no compiling, and allows the user to use variables, numeric functions, string functions, and logical operators.

Awk is a utility that enables a programmer to write tiny but effective programs in the form of statements that define 
text patterns that are to be searched for in each line of a document and the action that is to be taken when a match is 
found within a line. Awk is mostly used for pattern scanning and processing. It searches one or more files to see if they 
contain lines that matches with the specified patterns and then performs the associated actions.

Awk is abbreviated from the names of the developers – Aho, Weinberger, and Kernighan.


WHAT CAN WE DO WITH AWK ?

1. AWK Operations:
(a) Scans a file line by line
(b) Splits each input line into fields
(c) Compares input line/fields to pattern
(d) Performs action(s) on matched lines

2. Useful For:
(a) Transform data files
(b) Produce formatted reports

3. Programming Constructs:
(a) Format output lines
(b) Arithmetic and string operations
(c) Conditionals and loops



solution
awk '{if(NR==10) print $0}' file.txt
"""
