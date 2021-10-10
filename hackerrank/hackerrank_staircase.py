"""
Staircase detail

This is a staircase of size 6:

     #
    ##
   ###
  ####
 #####
######
"""


# def staircase(n):
#     for i in range(n):
#         blanks = ' ' * (n-i-1)
#         hashtag = '#'* (i+1)
#         print(f'{blanks + hashtag}')

# Refractored
def staircase(n):
    for i in range(n):
        print(' '*(n-i-1) + '#'*(i+1) )

if __name__ == '__main__':
    n=6
    staircase(n)
