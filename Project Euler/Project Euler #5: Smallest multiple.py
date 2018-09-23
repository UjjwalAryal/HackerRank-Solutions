def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)
t=input()
for i in range(t):
    n=input()
    fact=1
    for j in range(1,n+1):
        fact*=(j/gcd(fact,j))
    print fact
