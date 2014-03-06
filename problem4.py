def isPalindrome(N):
    S = str(N)
    L = len(S)
    for i in xrange(L):
        if S[i] != S[L-1-i]: return False
    return True

max = 0
for i in range(100,1000):
    for j in range(100,1000):
            if isPalindrome(i*j) and max < i*j: max = i*j

print max

