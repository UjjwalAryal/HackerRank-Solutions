def abs(x):
    if x<0:
        return -x
    return x

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print abs(n*(n+1)*(n+2-3*n**2))/12
