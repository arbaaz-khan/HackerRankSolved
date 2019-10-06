def maxUnqiueStones(input1,input2,input3):
    n_weights = set(map(int, input3[1:-1].split(",")))
    m_weights_set = set([i for i in range(1, input1 + 1)])
    set_diff = m_weights_set - n_weights
    weights = list(set_diff)
    w = 0
    ct = 0
    i = 0
    while ct <= input1 and w <= input1:
        w += weights[i]
        ct += 1
        i += 1
    if w > input1 or ct > input1:
        ct -= 1
    print(ct)

input1 = int(input())
input2 = int(input())
input3 = input()
maxUnqiueStones(input1, input2, input3)