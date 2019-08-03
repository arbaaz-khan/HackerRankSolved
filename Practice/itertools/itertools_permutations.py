#https://www.hackerrank.com/challenges/itertools-permutations/problem
from itertools import permutations
strL = input().split()
str = sorted(strL[0])
res = list(permutations(str,int(strL[1])))
for i in range(len(res)):
    print(''.join(res[i]))