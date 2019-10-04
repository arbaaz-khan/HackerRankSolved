# Find the total water trapped between the buildings.
'''
    INPUT: 1,2,3,1,2,1,3 (building heights)
    OUTPUT: 5
'''
h = list(map(int, input().strip().split(",")))
w = 0
for i in range(1, len(h)-1):
    lm = max(h[0:i])
    rm = max(h[i+1:len(h)])
    m = min(lm, rm)
    if m > h[i]:
        w += m-h[i]
print("Trapped water:", w)

# LOGIC: Need to calculate the water trapped in each building,
# for this we need to calculate the highest buildings in both sides,
# of the same building and find the minimum out of the two, the difference
# between the minimum one and the current building height(only if the current
# building's height is smaller than the minimum) is the water trapped over
# that building.
