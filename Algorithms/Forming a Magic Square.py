def check(x,y):
    s=0
    for i in range(9):
        if x[i]>y[i]:
            s+=x[i]-y[i]
        else:
            s+=y[i]-x[i]
    return s

a=[[4,9,2,3,5,7,8,1,6],[4,3,8,9,5,1,2,7,6],[2,9,4,7,5,3,6,1,8],[2,7,6,9,5,1,4,3,8],[6,1,8,7,5,3,2,9,4],[6,7,2,1,5,9,8,3,4],[8,1,6,3,5,7,4,9,2],[8,3,4,1,5,9,6,7,2]]
n1=map(int,raw_input().strip().split(' '))
n2=map(int,raw_input().strip().split(' '))
n3=map(int,raw_input().strip().split(' '))
n=n1+n2+n3
res=check(n,a[0])
for i in range(1,8):
    if check(n,a[i])<res:
        res=check(n,a[i])
print res
