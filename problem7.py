i = 3
prime = [2]
flag = 0

while(1):
    for j in prime:
        if i%j == 0: flag = 1
    if flag == 0:
        prime.append(i)
    flag = 0
    i+=1

    if len(prime) == 10001: break

print prime[10000]
