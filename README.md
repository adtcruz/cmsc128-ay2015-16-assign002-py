##CMSC128 Assignment 002
This is a submission to a requirement in CMSC128 -- Introduction to Software Engineering -- of the Academic Year 2015-2016. Written in Python, this is a library which could be used in Simple Bioinformatics Problems. 

Feel free to use this library if you find it useful for your project.

####Files included
* This document, README.md
* getHammingDistance.py
* countSubstrPattern.py
* isValidString.py
* getSkew.py
* getMaxSkewN.py
* getMinSkewN.py

####How to use
Each of the Python scripts included have the test cases given by our lecturer. Simply invoke 'python <filename>' to test these functions. These are tested to run in Python 2.7.5.

If you wish to use these functions in your project, simply comment out those lines that are marked by the '#test case' comment by adding a number symbol('#') in the line start.

######getHammingDistance.py
This contains a function counts the number of characters that differ between two strings of equal length. String length must never be less than 1.

######countSubstrPattern.py
This contains a function that counts the number of occurence of a pattern in a string.

######isValidString.py
This contains a function that checks if a string is valid given a string that includes the accepted letters. The arguments for the function is case-sensitive.

######getSkew.py
This contains a function that counts the number of Gs minus the number of Cs in a genome string in the first n nucleotides.

######getMaxSkewN.py
This contains a function that returns the maximum skew in the first n nucleotides.

######getMinSkewN.py
This contains a function that returns the minimum skew in the first n nucleotides.
