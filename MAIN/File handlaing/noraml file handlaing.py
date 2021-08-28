# with open('first.txt', 'w') as file:
#     file.write('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eos molestias ea sit veniam, rerum, totam quis eaque excepturi aut, nostrum reiciendis. At, harum quos adipisci magni nesciunt aliquid beatae sit!')

# with open('first.txt', 'r') as file:
#     print(file.read())

# with open('first.txt', 'r+') as file:
#     file.write("\nI'm at the beginning\n")
#     file.seek(2)
#     file.write("\nI'm in the middle\n")
#     file.seek(0)
#     print(file.read())

# r+ read and write but when write not overwrite.
with open('first.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write("la;l")
    file.read()

with open('text2.txt','w+') as file:
    file.write("jdafjafoomo\ndafdgf\ndgdg\ntee")
    # file.write("\nI'm at the end\n")
    file.seek(3)
    print(file.read())

# with open('first.txt', 'w+') as file:
#     file.write("Now everything is overwritten :(")
#     file.seek(0)
#     print(file.read())

