import sys
sys.stdout.write("Hello,")
sys.stdout.write("World! \n")
print("Hello, ", end="")
print("World!")
for line in sys.stdin:
    print(line)