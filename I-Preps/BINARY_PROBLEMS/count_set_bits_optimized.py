#Brian Kernighan’s Algorithm
# When we subtract 1 from a number then all the right bits starting from the right most set bit
# get flipped.
# 10 = 1010
# 9  = 1001
# 8  = 1000
# 7  = 0111
# So, if we keep on subtracting 1 from n and do (n & n-1) till we get (n & n-1) = 0, each time
# incrementing a counter, we have the total number of set bits.
# TIME COMPLEXITY: O(N) in worst case, but out performs all other algorithms in average & best cases

n = int(input())
def countSetBits(n):
    ct = 0
    while(n != 0):
        n &= (n-1)
        ct += 1
    return ct

print(countSetBits(n))