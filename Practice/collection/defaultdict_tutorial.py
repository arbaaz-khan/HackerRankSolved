# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
#BY USING DEFAULTDICT
from collections import defaultdict
d = defaultdict(list)
n_m = list(map(int,input().strip().split(" ")))
for i in range(n_m[0]):
    d[input()].append(str(i+1))
for i in range(n_m[1]):
    x = input()
    if d[x] != []:
        print(' '.join(d[x]))
    else:
        print("-1")
#WITHOUT USING DEFAUTDICT
'''
INPUT:
5 2
a
a
b
a
b
a
b
OUTPUT:
1 2 4
3 5
'''