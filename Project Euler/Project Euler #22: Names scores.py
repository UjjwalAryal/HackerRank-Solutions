alphabets = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def value(s):
    v = 0
    for i in s:
        v += alphabets.index(i)
    return v

str = []
for _ in xrange(input()):
    str.append(raw_input().strip())

str.sort()
for _ in xrange(input()):
    x = raw_input().strip()
    print value(x) * (str.index(x) + 1)  
