#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int,input().split()))
m = int(input())
for i in range(m):
    c = input().strip().split()
    if c[0] == "pop":
        s.pop()
    elif c[0] == "discard":
        s.discard(int(c[1]))
    elif c[0] == "remove":
        s.remove(int(c[1]))
sum = 0
for i in range(len(s)):
    sum += s.pop()
print(sum)