'''
TODO: Need to uptimize
You are given a binary string a s string containing Os and 1s) You need to determine the number of substrings of
that would have at least X set bits.

Input format

First line: T is the number of test cases. Each test case is followed by 3 lines.

In each test case

First line: Integer N denoting the size of the binary string
Second line: Binary string S

Third line: Single Integer X, as mentioned in the question

Output format

For every test case, print the required answer in a new line.
'''

t = int(input())
def count(n):
    if (n == 0):
        return 0
    else:
        return (n & 1) + count(n >> 1)

for ts in range(0,t):
    n = int(input())
    arr = input()
    m = int(input())
    ct = 0
    for i in range(0, n):
        for j in range(i, n):
            if count(int(arr[i:j+1],2)) >= m:
                ct += 1
    print(ct)



