#https://www.hackerrank.com/challenges/kangaroo/problem

# Python solution 
def kangaroo(x1,v1,x2,v2):
    if x1 < x2 and v1 < v2:
        return "NO"
    else:
        if v1 != v2 and (x2-x1)%(v2-v1)==0:
            return "YES"
        else:
            return "NO"


print(kangaroo(21,6,47,3))
print(kangaroo(28,8,96,2))
print(kangaroo(14,4,98,2))



"""
Javascript Solutions

// Smart way
function kangaroo(x1,v1,x2,v2){
    console.log(x1,v1,x2,v2)
    if (x1 < x2 && v1 < v2){
        return "NO"
    } else {
        if (v2 != v1 && (x2 - x1)%(v2-v1) == 0) {
            return "YES"
        } else {
            return "NO"
        }
    }
}

// rough way
function kangaroo(x1,v1,x2,v2){
    for(let i=0; i < 100; i++){
        x1 += v1
        x2 += v2

        return x1 == x2 ? "YES":"NO"
    }
}
console.log(kangaroo(0,2,5,3))


"""
