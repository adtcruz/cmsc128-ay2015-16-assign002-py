#Damn, I realised that Python does not support bloody UTF-8 characters, oh well..
#!/usr/bin/python
#AUTHOR: CRUZ, Anton Dominique T.
#SUBJECT: CMSC128 Introduction to Software Engineering
#SECTION: AB-7L
#DESCRIPTION: File for the countSubstrPattern function

def countSubstrPattern(original, pattern): #defines the countSubstrPattern function
   if len(original) < len(pattern): #if the pattern has more characters than the original, return 0
      return 0
   else: #checks for the substring pattern and counts the number of matches
      i = 0 #initialises the i index to nought
      skipletter = 0 #variable used for counting or discarding the substring match count
      ulimit = len(original) - len(pattern) + 1 #upper limit for loop controlling the search
      sbstrnm = 0 #substring match count
      while i < ulimit: #loop that searches for substring matches
         if original[i] == pattern[0]: #if the letter at index i matches the first letter of the pattern
            j = 1 #sets j to 1
            h = i + 1 #sets h to i + 1
            while j < len(pattern): #loop that checks if the next letters match the rest of the pattern 
               if original[h] == pattern[j]: #if the letter at index h of the original and letter at index j of the pattern matches, increment j and h
                  j = j + 1
                  h = h + 1
               else: #if they do not
                  skipletter=1 #sets skipletter to 1
                  break #stop the loop
            if skipletter == 1: #if skipletter is set to 1, set skipletter to zero
               skipletter = 0
            else:
               sbstrnm = sbstrnm + 1 #if skipletter's not set to one, a match was found so we increment the substring matches count by 1
            i = i + 1 #increments index i
         else: #if the letter at index i does not match the first letter of the pattern
            i = i + 1 #increments index i
      return sbstrnm #returns the substring match count     
   return

print countSubstrPattern(original="AATATATAGG",pattern="GG") #test cases from Sir Regi
print countSubstrPattern(original="AATATATAGG",pattern="ATA") #test cases from Sir Regi
print countSubstrPattern(original="AATATATAGG",pattern="ACTGACTGACTG") #test cases from Sir Regi
