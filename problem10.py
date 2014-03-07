i = 3
prime = [2]
flag = 0

while(1):
    for j in prime:
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        prime.append(i)
    flag = 0
    if i >= 2000000: break
    i += 1

print sum(prime)
