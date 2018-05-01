# for i in 'ABC':
#     print(i)
def findMinAndMax(nums):
    max=nums[0]
    min=nums[0]
    for i in nums:
        if i > max:
            max=i
        if i < min:
            min=i
    return (max,min)
print(findMinAndMax([9, 7, 1, 10, 56, 89, 555, 454, 559, -1, 0]))

# def findMinAndMax(L):
#     # if len(L) == 0:
#     #     return(None, None)
#     mi = L[0]
#     mx = L[0]
#     for l in L:
#         if mi>l:
#             mi=l
#         if mx<l:
#              mx=l
#     return(mi,mx)
#
# print(findMinAndMax([9, 7, 1, 10, 56, 89, 555, 454, 559, -1, 0]))
from collections import Iterable