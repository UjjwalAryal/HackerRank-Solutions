n,k=map(int,list(raw_input().split(' ')))
x=map(int,list(raw_input().split(' ')))
if k<max(x):
    print max(x)-k
else:
    print 0
