N = 600851475143
i = 2
A = 0

while(1):
    if N%i == 0:
        A = N
    i+=1
    if i == 600851475143: break


print A
