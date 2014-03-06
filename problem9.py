canditate=[]

for x in xrange(1,200):
    for y in xrange(1,200):
        for z in xrange(1,200):
            if 3*x+4*y+5*z == 1000: canditate.append([x,y,z])

print canditate
"""
for i in canditate:
    if (3*x)**2+(4*y)**2 == (5*z)**2: print 3*x*4*y*5*z
