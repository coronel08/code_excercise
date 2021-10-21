# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    answer = []
    for i in grades:
        if i >= 38 and i % 5 > 2:
            answer.append ((5 - (i%5)) + i)
        else:
            answer.append (i)
    return answer

# list1 = [57,97,56,81,38,30,1,9,23,69,24,44,69,12,61,50,84,3,17]
list2 = [44,73, 67, 38, 33]
print(gradingStudents(list2))



"""
// javascript solution

function gradingStudents(grades){
    let list1 = []
    
    for(let i of grades){
        console.log(i)
        if (i >=38 && i%5 > 2){
            list1.push((5 - (i%5)) + i)
        } else {
            list1.push(i)
        }
    }
    return list1
}

let list2 = [44,73, 67, 38, 33]

console.log(gradingStudents(list2))

"""
