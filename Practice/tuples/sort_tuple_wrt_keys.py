tuples = [(3, 2), (1, 6), (9, 1), (2, 3)]
def sortkey(t):
    return t[0]

# tuples = sorted(tuples, key = sortkey)
tuples = sorted(tuples, key = lambda t: t[0])
print(tuples)