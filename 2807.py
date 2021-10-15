#2807 - Iccanobif

n = int(input())
mfib = []
def fibonacci_of(n):
    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    previous, fib_number = 0, 1
    mfib.append(fib_number)
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number
        mfib.append(fib_number)

    return fib_number

fibonacci_of(n)
rmfib = mfib[::-1]

for x in range(len(rmfib)):
    if x < len(rmfib)-1:
        print(rmfib[x], end=" ")
    else:
        print(rmfib[x])