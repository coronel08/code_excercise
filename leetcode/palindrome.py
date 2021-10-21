"""
https://leetcode.com/problems/valid-palindrome/submissions/

A palindrome is a string or word that is the same backwards
"""



import re


# below is a one liner that strips everything that is not a letter, and then combines it
# test2 = ''.join([i for i in string if i.isalpha()])

def isPalindrome(string):
  s = string.lower()  
  text = re.sub("[^a-zA-Z0-9]+", "",s)
  revText = lambda i: i[::-1]
  if text == revText(text):
    return True
  else:
    return False
    
