s=0

for i in range(1,1000):
    if i%15==0:
        print i,
        s+=i
    else:
        if i%5==0:
            print i,
            s+=i
        if i%3==0:
            print i,
            s+=i

print s