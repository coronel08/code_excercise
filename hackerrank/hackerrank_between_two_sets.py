# https://www.hackerrank.com/challenges/between-two-sets/problem
# list b needs to be divisble by the # while also being a multiple of list a


def getTotalX(a,b):
    list_a = []
    list_b = []
    max_a,min_b = max(a), min(b)
    for i in range(max_a,min_b + 1):
        if all([i % a_item == 0 for a_item in a]):
            list_a.append(i)
        if all([b_item % i == 0 for b_item in b]):
            list_b.append(i)
    print(list_a, list_b)
    answer = [value for value in list_a  if value in list_a and list_b]
    # refractored into the above
    # answer = [x for x in list_a + list_b if x in list_a and x in list_b]
    # answer = set(list_a).intersection(list_b)
    return print((len(set(answer))))
         
a = [3,9,6]
b=[36,72]
# a = [3,4]
# b = [24,48]
getTotalX(a,b)



# algo used for dividing b by a then dividing results by a.
# def getTotalX(a,b):
#     a,b = sorted(a), sorted(b)
#     common_list = set()
#     answer_list = []
#     for b_item in b:
#         for a_item in a:
#             if b_item % a_item == 0:
#                 common_list_math = b_item // a_item
#                 common_list.add(common_list_math)
#                 if common_list_math % a_item == 0:
#                     answer_list.append(common_list_math)
    
#     print(common_list)
#     print(set(answer_list))
