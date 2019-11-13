"""
**********
unix grep*
**********
The grep command is used to search text. It searches the given file for lines containing a match to the given strings or words.
It is one of the most useful commands on Linux and Unix-like system. Let us see how to use grep on a Linux or Unix like system.

**********************
grep command examples*
**********************
Common grep command explained with examples in Linux:
- grep 'word' filename – Search any line that contains the word in filename on Linux
- grep -i 'bar' file1 – A case-insensitive search for the word ‘bar’ in Linux and Unix
- grep -R 'foo' . – Search all files in the current directory and in all of its subdirectories in Linux for the word ‘foo’
- grep -c 'nixcraft' frontpage.md – Search and display the total number of times that the string ‘nixcraft’ appears in a file named frontpage.md



solution

grep "^\(\([0-9]\{3\}-\)\|\(([0-9]\{3\}) \)\)[0-9]\{3\}-[0-9]\{4\}$" file.txt
"""