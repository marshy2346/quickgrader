# QuickGrader
__Version: 1.0__

__TODO__: Make this documentation better.

<br/>


__New Features__:
 <br/>
    __GUI Mode__
     add --gui-mode flag
    This mode walks through all of the student submissions and allows you to run terminal commands. It
    also provides some utility commands which include,
    >
    >    r <filename>.java - to compile and run a java file
    >    e                 - to record the students submission in the error file
    >    n                 - go to next student
    >    c <message>       - write comment for student
    >    h                 - display help prompt
    >

    `

__Instructions__:

__(1)__ Go to python script directory

__(2)__ Add driver file to directory

__(3)__ Add expected output text file to directory

__(4)__ Add optional input file to directory

__(5)__ Record all names in config.py

__(6)__ In same directory, run python3 main.py

__Walkthrough__:

__(1)__ The script will run the diff on each student's assignment
(compare expected output and program output).

__(2)__ After, the script will prompt you to add a comment.

__(3)__ Rinse and repeat.


 - All comments will be in comments.csv file

 - All folders with errors will be recorded in errors.txt


	Note: If the driver program has non-deterministic output, the driver will
	have to be modified in order for the program to be helpful.
