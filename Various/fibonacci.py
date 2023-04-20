
# Fibonacci sequence from 1 to n

def getFibonacciList(n):
    """Return a list containing the Fibonacci series up to n."""
    r = []
    a, b = 0, 1
    while (a < n):
        r.append(a)
        a, b = b, a+b
    return r

print("\nFibonacci Sequence Program \n")
n = int(input("Enter the value of n : "))
fib = getFibonacciList(n)
print("\nFibonacci up to ", n, " is : ", fib, "\n")
