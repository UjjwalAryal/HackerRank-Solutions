for _ in xrange(input()):
    n , k = map(int,raw_input().strip().split(' '))
    l = map(int, list(raw_input().strip().split(' ')[0]))
    print max(map(lambda i: reduce(lambda x,y: x*y, l[i:i+k]),range(len(l)-k)))
