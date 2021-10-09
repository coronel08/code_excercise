"""
https://www.hackerrank.com/challenges/find-a-string/problem
You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
"""

def count_substring(string, sub_string):
    total = 0
    for x in range(len(string)):
        sub_string_length = len(sub_string)
        if string[x:x+sub_string_length] == sub_string:
            print(string[x:x+sub_string_length])
            total += 1
    return(total)
        
# string= 'ABCDCDC'
# sub_string = 'CDC'

string= 'ThIsisCoNfUsInG'
sub_string = 'is'
    
count = count_substring(string, sub_string)
print(count)



