# Prints all the n numbers in the fibonacci series.
n = int(input())
f1 = 0
f2 = 1
if n==0:
    print(f1)
elif n==1:
    print(f2)
else:
    #print(f1, f2,end=" ")
    for i in range(2,n+1):
        temp = f2
        f2 = f1 + f2
        f1 = temp
        #print(f2,end=" ")
print(f2)