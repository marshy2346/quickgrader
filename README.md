# QuickGrader
__Version: 1.1__
<br/>

A helper script I use to facilitate grading student's java programs. 

__TODO__: Make this documentation better.

<br/>


__New Features__:
<br/>
 <br/>
__GUI Mode__<br/>

    add --gui-mode flag
This mode walks through all of the student submissions and allows you to run terminal commands. It
also provides some utility commands which include,

    r <filename>.java - to compile and run a java file
    e                 - to record the students submission in the error file
    n                 - go to next student
    c <message>       - write comment for student
    h                 - display help prompt


__Instructions__:

1. Go to python script directory
2.  Add driver file to directory
3.  Add expected output text file to directory
4.  Add optional input file to directory
5. Record all names in config.py
6. In same directory, run python3 main.py

__Walkthrough__:

1. The script will run the diff on each student's assignment
(compare expected output and program output).
2. After, the script will prompt you to add a comment.
3. Rinse and repeat.


> All comments will be in comments.csv file 
>
>
>All folders with errors will be recorded in errors.txt

	Note: If the driver program has non-deterministic output, the driver will
	have to be modified in order for the program to be helpful.
