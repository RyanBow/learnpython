while True:
    try:
        x = int(input("First:"))
        y = int(input("Second:"))
        print(x / y)
    except Exception as e:
        print(e)
        print('again')
    else:
        break