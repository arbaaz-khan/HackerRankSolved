#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    s = set(array)
    avg = 0
    for h in s:
        avg += h
    return avg/len(s)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)