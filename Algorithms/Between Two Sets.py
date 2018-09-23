def factor(x,a):
    for i in x:
        if a%i!=0:
            return 0
    return 1
def Isfactor(x,a):
    for i in x:
        if i%a!=0:
            return 0
    return 1

n,m = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))
l=[]
for i in range(max(a),min(b)+1):
    if factor(a,i) and Isfactor(b,i):
        l.append(str(i))
print len(l)       
