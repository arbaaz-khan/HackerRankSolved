# Find the subarray with the maximum sum (contiguous)
'''
    INPUT:  1,-2,-4,2,1,-1,4
    OUTPUT: 6
'''
a = list(map(int, input().strip().split(",")))
gMax = -99999999
for i in range(0, len(a)):
    lMax = -99999999
    sum = 0
    for j in range(i, len(a)):
        sum += a[j]
        if lMax < sum:
            lMax = sum
    if gMax < lMax:
        gMax = lMax
print(gMax)
'''
LOGIC:
1,-2,-4,2,1,-1,4
->
->->
-> -> ->
..............->
   ->
   ->->
   ...........->

Update the local max sum
Finally update the global max sum
'''