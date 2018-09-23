x1,v1,x2,v2 = map(float,raw_input().strip().split(' '))
print 'YES' if (v1>v2 and (x1-x2)%(v1-v2)==0) else 'NO'
