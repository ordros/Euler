from math import sqrt

a = (1+sqrt(5))/2
b = (1-sqrt(5))/2
r = 0

i = 1
s = 0
while 1:
    r = int((1/sqrt(5))*(a**i-b**i))
    if r>=4000000: break
    if r%2 == 0:
        s += r
    i+=1
print s
