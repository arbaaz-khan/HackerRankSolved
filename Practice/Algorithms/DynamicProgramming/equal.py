# Need to have a complete understanding

def findMin(n):
    min = 0
    if n >= 5:
        min += n//5
        n = n%5
    if n >= 2:
        min += n//2
        n = n%2
    min += n
    #print(min)
    return min

def equal(arr):
    globalMin = 9999999
    for i in range(len(arr)):
        if arr[i] < globalMin:
            globalMin = arr[i]
    res = 9999999
    for i in range(5):
        min = 0
        for j in range(len(arr)):
            min += findMin(arr[j]-globalMin+i)
        if min < res:
            res = min
    #print(res)
    return res

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        print(str(result)+"\n")
