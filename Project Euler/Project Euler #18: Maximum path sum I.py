def max_path(l,i,j):
    if(i == len(l)-1):
        return l[i][j]
    return max(l[i][j] + max_path(l,i+1,j),l[i][j] + max_path(l,i+1,j+1))

for _ in xrange(int(raw_input())):
    l = []
    for __ in xrange(int(raw_input())):
        l.append(map(int,raw_input().strip().split(' ')))
    print(max_path(l,0,0))
