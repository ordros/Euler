def isPrime(N):
    if N%2 == 0: return False
    return (2**(N-1))%N == 1

j = 0
for i in range(2,1000000):
    if isPrime(i): j+=1
    if j==10001: break

print i
