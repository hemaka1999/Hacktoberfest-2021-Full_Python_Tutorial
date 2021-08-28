import dis
def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)
# Display the disassembled bytecode of the function.
dis.dis(fib)
print(fib.__code__)
dir(fib.__code__)