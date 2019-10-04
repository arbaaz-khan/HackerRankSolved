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
