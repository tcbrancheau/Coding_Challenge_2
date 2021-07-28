Prerequisites:
This project was created using Python 3.9.6.

Installation:
To install this project, clone "Secureworks_Coding_Challenge" from
https://github.com/tcbrancheau/Secureworks_Coding_Challenge.git to a
directory on your machine.

Running:
To run this project, I created the ProgramRunner.py script.  To run
this script, execute the following from the command line inside the
directory where the project files are located:
    python ProgramRunner <data_file_name>
where <data_file_name> is the name of the file with data you want the
program to process.  ProgramRunner.py was created based on the
specifications of the assignment.

To run the tests in this project, execute the following  from the command
line inside the directory where the project files are located:
    python -m unittest

To run just the tests inside a file, run:
    python -m unittest <file_name>
where <file_name> is the name of the file with the tests.

Project Summary:
The purpose of this project is to create a python program that can read in
data from a file, separate that data into words, determine the longest word
or words in the file, and print out the word along with the reverse of that
word.

There are tests for each method of the two classes in this project to ensure
it is working as designed.

Project Assumptions:
First off, this project assumes the input will always be of type str.  This
input can come from a file or a file-like object.

Secondly, this project did not create exceptions for the conditions when the
input has no words.  An error message is printed to guide the user in the event
there is no data found.  There are also no exceptions for a user attempting to
send in the wrong type of input.  Again, an error message printed to stdout
should help the user understand the issue.

