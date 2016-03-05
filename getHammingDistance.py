#Damn, I realised that Python does not support bloody UTF-8 characters, oh well..
#!/usr/bin/python
#AUTHOR: CRUZ, Anton Dominique T.
#SUBJECT: CMSC128 Introduction to Software Engineering
#SECTION: AB-7L
#DESCRIPTION: File for the getHammingDistance function

def getHammingDistance(str1, str2): #defines getHammingDistance function
   hammingDistance = 0 #sets a local variable named hammingDistance and initialise it to nought
   if len(str1) == len(str2): #checks if the strings are of equal length
      i = 0; #sets an index variable to zero
      for letter in str1: #traverses each letter of the first string
         if letter == str2[i]: #if the letters at index i match, proceed to the next letter 
            i = i + 1
            continue
         else: #if the letters at index i do not match, increment the hammingDistance
            i = i + 1
            hammingDistance = hammingDistance + 1
            continue
   else: #if the strings are not of equal length, return an error message
      return "Error! Strings are not equal!"
   return hammingDistance;

print getHammingDistance(str1="AACCTT",str2="GGCCTT") #test cases from Sir Regi
print getHammingDistance(str1="TCGGA",str2="AAAAG") #test cases from Sir Regi
print getHammingDistance(str1="A",str2="AG") #test cases from Sir Regi
