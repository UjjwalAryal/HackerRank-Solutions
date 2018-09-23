t=input("")
for i in range(0,t):
    n=input("")
    t1,t2,sum=1,1,0
    t3=t1+t2
    while t3<=n:
        if t3%2==0: sum+=t3
        t1,t2=t2,t3
        t3=t1+t2
    print sum
