import time

N = 600851475143

def factor(N):
    for i in range(2,1000000):
        if N%i == 0:
            print i
            break
    if N/i != 1:
        factor(N/i)

factor(N)