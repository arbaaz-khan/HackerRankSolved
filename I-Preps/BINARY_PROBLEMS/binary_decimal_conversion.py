# Binary to decimal
# Built in
b = "100111"
d = int(b, 2)
print(b, 'in decimal =', d)
# Logic
d = 0
for i in range(len(b)-1, -1, -1):
    d += int(b[i]) * 2**(len(b)-1-i)
print(d)


# Decimal to binary
d = 52
b = bin(d).lstrip('0b')  # or bin(d).replace("0b","")
print(d, 'in binary = ', b)

# Logic
b = ""
while d != 0:
    b = str(d % 2) + b
    d = d//2
print(b)
