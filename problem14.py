C = 0
def collatz(N):
    global C
    C+=1
    if N == 1:
        return
    if N%2 == 0: collatz(N/2)
    else: collatz(3*N+1)

max = 0
i_max = 0
for i in range(1,1000000):
    collatz(i)
    if max < C:
        max = C
        i_max = i
    C = 0

print i_max