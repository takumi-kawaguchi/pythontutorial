while True:
    try:
        int(input('enter a number: '))
        break
    except ValueError:
        print("invalid number entered")