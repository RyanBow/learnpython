try:
    x = int(input("First:"))
    y = int(input("Second:"))
    print(x / y)
except ZeroDivisionError:
    print('second is zero')