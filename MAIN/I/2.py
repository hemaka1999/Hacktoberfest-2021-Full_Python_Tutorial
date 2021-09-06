import fileinput

for line in fileinput.input():

    if line=="off":
            print('end')
    print(line)
