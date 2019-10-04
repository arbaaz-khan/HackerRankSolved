'''
You are given an array A of N elements. You have performed Q queries in it. In each query, you select an index I-based) and perform the following
operation:

for j = I + 1 to N:
    if A[j]<A[I]:
        A[j] = 0

You are required to print the version of array A after all the Q queries are processed

Note: The queries are not independent of each other. Therefore. you are required to use the updated array A. for each query.

Input format

First line: An integer T denoting the number of test cases
For each test case

First line: 2 space-separated integers N and Q denoting the number of elements in the array and number of queries
9 Second line: N space-separated integers denoting the elements in the initial array A
a Third line: Q space-separated integers denoting the selected index in each query

Output format
For each test case print N space-separated integers denoting the final array A in a separate line.

'''
def final_arr(A, query, q, N):
    for j in range(q):
        for k in range(query[j] +1, N):
            if A[k] < A[q]:
                A[k] = 0
    return A

T = int(input())
for i in range(T):
    arr1 = list(map(int, input().split()))
    N = arr1[0]
    q = arr1[1]
    A = list(map(int, input().split()))
    query = list(map(int, input().split()))
    out_ = final_arr(A, query, q,  N)
    print(' '.join(map(str, out_)))
