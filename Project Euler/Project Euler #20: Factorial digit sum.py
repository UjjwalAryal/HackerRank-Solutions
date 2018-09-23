def fact(n):
    try:
        return reduce(lambda x,y: x*y, xrange(1,n+1))
    except:
        return 1
for _ in range(input()):
    print sum(map(int, str(fact(input()))))
