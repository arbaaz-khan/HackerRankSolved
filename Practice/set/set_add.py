#https://www.hackerrank.com/challenges/py-set-add/problem
n = int(input())
ct = 0
stamps = set()
for i in range(n):
    stamps.add(input())
print(len(stamps))
