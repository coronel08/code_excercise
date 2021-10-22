# https://www.hackerrank.com/challenges/sock-merchant/submissions/code/239528888

# store value and count in a dict, if div by 2 increase count. 
def sockMerchant(n, ar):
    test = {}
    count = 0
    # Dict comprehension below
    # test2 = {k:ar.count(k) for (k) in ar}
    for i in ar:
        test[i] = test.get(i, 0) +1
        if test[i] % 2 == 0:
            count += 1
    return (count)
  
  
  
  
  """
 Javascript Solution below, store values and count in a dict, count if divisible by 2 
  
  
  function sockMerchant(n, ar) {
    let test = {}, count = 0
    for(let sock of ar){
        test[sock] = ((test[sock] || 0) +1)
        test[sock] % 2 == 0 ? count += 1:""
    }
    return (count)
}
  """
