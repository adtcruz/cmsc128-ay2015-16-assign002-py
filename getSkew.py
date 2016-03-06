#Damn, I realised that Python does not support bloody UTF-8 characters, oh well..
#!/usr/bin/python
#AUTHOR: CRUZ, Anton Dominique T.
#SUBJECT: CMSC128 Introduction to Software Engineering
#SECTION: AB-7L
#DESCRIPTION: File for the getSkew function

def getSkew(str, n): #defines getSkew function
   if n < 1:
      print "n has to be greater than 0"
      return -1
   i = 0 #initialises the index i for traversing str
   j = n - 1 #initialises the position where traversing shall end
   gCount = 0 #initialises the number of Gs
   cCount = 0 #initialises the number of Cs
   while i <= j: #traverses str until the end position
      if str[i] == "G": #if the character is a G, increment gCount
         gCount = gCount + 1
      elif str[i] == "C": #if the character is a C, increment cCount
         cCount = cCount + 1
      i = i + 1 #increments i before going looping again
   skew = gCount - cCount #computes for the skew by subtracting the number of Gs from the number Cs at the given postion
   return skew #returns the skew

print getSkew(str="GGCCAC",n=1) #test cases from Sir Regi
print getSkew(str="GGCCAC",n=2) #test cases from Sir Regi
print getSkew(str="GGCCAC",n=3) #test cases from Sir Regi
print getSkew(str="GGCCAC",n=4) #test cases from Sir Regi
print getSkew(str="GGCCAC",n=5) #test cases from Sir Regi
