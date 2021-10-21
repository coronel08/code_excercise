# https://www.hackerrank.com/challenges/migratory-birds/problem

arr = [1,1,2,2,3]

def migratoryBirds(arr):
    # dct = {i: arr.count(i) for i in arr}
    dct = {}
    for i in arr:
        if i not in dct:
            dct[i] = arr.count(i)

    maxValue = (max(dct.values()))
    
    # Generator function below to return just one
    # maxValueList =  next((k for k,v in dct.items() if v == maxValue), None)
    # Generator fucntion below, use list to print all matches
    maxValueList =  list(k for k,v in dct.items() if v==maxValue)
    return min(maxValueList)


print(migratoryBirds(arr))


"""
Javascript Solution


"""
