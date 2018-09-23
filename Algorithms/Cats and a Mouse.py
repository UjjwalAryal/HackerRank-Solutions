import sys
def abs(x):
    if x<0:
        return -x
    return x

q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if abs(x-z)<abs(y-z):
        print "Cat A"
    elif abs(x-z)==abs(y-z):
        print "Mouse C"
    else:
        print "Cat B"
