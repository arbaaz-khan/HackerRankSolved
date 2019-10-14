# Prints all the nth number in the fibonacci series.

ct = 0
def fib(n,m):
    global ct
    #print(ct, m)
    ct += 1
    if m[n] != -1:
        return m[n]
    if n == 0:
        m[n] = 0
        return 0
    elif n == 1:
        m[n] = 1
        return 1
    else:
        m[n - 1] = fib(n - 1,m)
        m[n - 2] = fib(n - 2,m)
        return m[n-1] + m[n-2]


if __name__ == "__main__":
    n = int(input())
    m = [-1 for i in range(0,n+1)]
    print("Fibonacci no.:", fib(n,m))
    print("Count:", ct)