"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem
The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.
Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.

Example

a = [1, 2, 3]
b = [3, 2, 1]
For elements *0*, Bob is awarded a point because a[0] .
For the equal elements a[1] and b[1], no points are earned.
Finally, for elements 2, a[2] > b[2] so Alice receives a point.
The return array is [1, 1] with Alice's score first and Bob's second.
"""


def compareTriplets(a, b):
    countA = 0
    countB = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            countA +=1
        elif b[i] > a[i]:
            countB += 1
    return countA, countB
    

// Refractored to one liner
def compareTriplets(a,b):
    result = [1 if x>y else -1 if  y>x else 0 for x,y in list(zip(a,b))]
    return result.count(1), result.count(-1)
