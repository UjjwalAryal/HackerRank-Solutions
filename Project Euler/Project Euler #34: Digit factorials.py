def fact(x):
    if x==0:
        return 1
    return reduce((lambda x,y:x*y),range(1,x+1))

def fact1(x):
     l=map(lambda x:fact(int(x)),list(str(x)))
     return reduce(lambda x,y:x+y,l)

n,sum=input(),0

for i in range(10,n+1):
    if fact1(i)%i==0:
        sum+=i
print sum
