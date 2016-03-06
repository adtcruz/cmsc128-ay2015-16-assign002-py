#Damn, I realised that Python does not support bloody UTF-8 characters, oh well..
#!/usr/bin/python
#AUTHOR: CRUZ, Anton Dominique T.
#SUBJECT: CMSC128 Introduction to Software Engineering
#SECTION: AB-7L
#DESCRIPTION: File for the isValidString function

def isValidString(str,alphabet): #defines isValidString function
   nextchar = 0 #variable for checking if the next character should be checked 
   for char in str: #loop for traversing each character in str
      for letter in alphabet: #loop for traversing each letter in the alphabet
         if char == letter: #if the selected character matches the selected 'letter'
            nextchar = 1 #check the next character
            break #quit traversing the letters in the alphabet
      if nextchar == 1: #if nextchar is 1, selected character is in the alphabet so it's to continue checking str for matches
         nextchar = 0 #reset nextchar to 0
      else: #if nextchar is 0 selected character is not in the alphabet so it'll have to return false
         return "false" #returns false to end checking str 
   return "true" #returns true if all of the characters in str is in the alphabet

print isValidString(str="AAGGCTATGC",alphabet="ACGT") #test cases from Sir Regi
print isValidString(str="AAGGCTATGa",alphabet="ACGT") #test cases from Sir Regi
print isValidString(str="ACGT",alphabet="ACGT") #test cases from Sir Regi
print isValidString(str="ACGT101_",alphabet="ACGT") #test cases from Sir Regi
print isValidString(str="091212345",alphabet="0123456789") #test cases from Sir Regi
