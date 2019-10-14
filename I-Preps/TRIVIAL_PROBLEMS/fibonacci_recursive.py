# Prints all the nth number in the fibonacci series.
ct = 0
def fib(n):
    global ct
    ct += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    n = int(input())
    print("Fibonacci no.:",fib(n))
    print("Count:",ct)