canditate=[]

for a in xrange(1,500):
    for b in xrange(1,500):
        for c in xrange(1,500):
            if a+b+c == 1000: canditate.append([a,b,c])

for i in canditate:
    if i[0]**2+i[1]**2 == i[2]**2: print i[0]*i[1]*i[2]