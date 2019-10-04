# Count the anagrams from a list of string
'''
    INPUT: "cat,bat,ball,bat,cat,llab,tab,atb,aa,aa,tac,atb"
    OUTPUT: 4
'''

from collections import defaultdict

arr = list(input().strip('"').split(","))
arr2 = list(set(arr))
dict = defaultdict(lambda: False)
ct = 0
for i in range(0, len(arr2)-1):
    if dict[arr2[i]]:
        continue
    for j in range(i+1, len(arr2)):
        if dict[arr2[j]]:
            continue
        if sorted(arr2[i]) == sorted(arr2[j]):
            ct += 1
            dict[arr2[j]] = True
print(ct)