n=input()
a,r,l=[],0,0
for i in range(n):
   a.append(map(int,raw_input().split(' ')))
for i in range(n):
    r+=a[i][i]
    l+=a[n-i-1][i]
print abs(l-r)
