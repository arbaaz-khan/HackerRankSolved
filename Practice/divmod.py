#https://www.hackerrank.com/challenges/python-mod-divmod/problem
a = int(input())
b = int(input())
res = divmod(a,b)
print("{}\n{}\n{}".format(res[0],res[1],res))
#print("{}\n{}\n({}, {})".format(a//b,a%b,a//b,a%b),end="")