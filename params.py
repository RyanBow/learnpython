# def print_params(*params):
#     print(params)
# print_params('Testing')# 这个为啥会打印出逗号
# print_params(1,2,3)
# print_params('tyr')
x = 1
def change_global():
    global x
    x = x + 1
change_global()
print(x)