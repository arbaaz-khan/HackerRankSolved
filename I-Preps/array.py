'''
You are given an array A of size N. You have to replace every A[i] with A[i] + A[i +1]. As the last element does
not have elements to its right, delete it from the array. You have to repeat this process until there is one element left
in the array. Find the last element in the array.

Input format
    First line: Integer N denoting the size of the array
    Second line: N space-separated Integers, the ith of which is A[i]

Output format

Print the last element modulo 10^9 + 7 in the array

Constraints
1< N <= 10^3
1 < A[i] <= 10^3

sample input:
3
1 2 3
output:
8

'''
arr = list(map(int,input().strip().split(" ")))
for i in range(1,len(arr)):
    for j in range(0, len(arr) - i):
        arr[j] += arr[j+1]
print((arr[0]%10**9) + 7)