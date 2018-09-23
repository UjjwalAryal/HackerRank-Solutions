fact = lambda n : reduce(lambda x,y:x*y ,range(1,n+1))
for _ in range(input()):
    m,n=map(int,raw_input().strip().split(' '))
    print (fact(m+n)/(fact(m)*fact(n)))%(10**9+7)
