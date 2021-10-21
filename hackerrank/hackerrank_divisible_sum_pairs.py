# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# Python Solution

arr = [1,2,3,4,5,6]

def divisibleSumPairs(n,k,arr):
    count = 0
    for i, num in enumerate(arr):
        for j in range(i+1, len(arr)):
            print(num, arr[j])

    return print(count)
divisibleSumPairs(0,5,arr)






"""
Javascript Solution, nested loop that if i is smaller than j, add them. Keeps from adding repeats

arr = [1,2,3,4,5,6]

function divisibleSumPairs(n,k,arr){
    count = 0
    for(let i=0; i < arr.length; i++){
        for(let j=0; j < arr.length; j++){
            if(i < j){
                if((arr[i]+ arr[j]) % k == 0){
                    count += 1
                }
            }
        }
    }
    return count
}
divisibleSumPairs(0,5,arr)
"""
