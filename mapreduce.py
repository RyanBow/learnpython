# from functools import reduce
# def multi(x,y):
#     return x * y
# def multired(L):
#     return reduce(multi , L)
# print(multired([5 , 7 , 9]))
def normalize(name):
 return name.capitalize()

L1=['juLie','BellA','eva','LISA']
L2=list(map(normalize,L1))
print(L2)