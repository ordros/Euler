from math import sqrt, ceil

def count_divisors(N):
    fact = 1
    j = 0
    max = ceil(sqrt(N))
    if N >= 3:
        while N!=1 and N%2==0:
            j += 1
            N /= 2
        i = 3
        fact *=(j+1)
        j = 0
        while N!=1 and i<=max:
            while N!=1 and N%i==0:
                j += 1
                N /= i
            fact *=(j+1)
            i += 2
            j = 0
        if N > max:
            fact *=2

    return fact

i = 0
j = 1
while 1:
    i += j
    j += 1
    if count_divisors(i) >= 500:
        print i
        break


