'''
# TODO: Need to uptimize
There are N buildings situated on a coordinate axis at positions X1, X2, ....Xn. The height of the ih building is
H If ith building collapses, then other buildings in the coordinate range [Xi + 1, Xi + Hi] both inclusive will also
collapse. This is a chain reaction and it pushes the other buildings too. Your task is to find the maximum coordinate
that each building reaches when it falls collapses.

Input format

First line: Single integer N denoting the number of buildings.

Second line: N integers X1, X2,.... XN denoting the coordinates of each building
Third line: N integers H1, H2,.... HN denoting the height of each building

Output format

For each building, print the output in a new line.

Constraints
1<=N<= 10^5
1<= Xi, Li<= 10^12

Note: The array X is always in an ascending order.

Sample Input
7
5 6 9 11 12 16 20
2 3 1 5 3 1 1
Sample Output
10
10
10
17
.
.

56911121620
'''
n = int(input())
x = list(map(int,input().strip().split(" ")))
h = list(map(int,input().strip().split(" ")))
for i in range(0,n):
    d = 0
    for j in range(i,n):
        if j == i or d >= x[j]:
            if d >= x[j] + h[j]:
                continue
            else:
                d = x[j] + h[j]
    print(d)
