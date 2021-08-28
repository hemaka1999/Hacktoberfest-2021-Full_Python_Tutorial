try:
    print('lovely')
    print(10/0)
    print(kk)
    print("kk")

except NameError:
    print('name not found')

except ZeroDivisionError:
    print("you can't divide by number in 0")

except IndentationError:
    print("indention error")

except IOError:
    print("input or output errorf")
