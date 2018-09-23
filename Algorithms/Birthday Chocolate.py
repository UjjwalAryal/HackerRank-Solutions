n=input()
l=map(int,raw_input().strip().split(' '))
d,m=map(int,raw_input().strip().split(' '))
c=0
for i in range(len(l)-m+1):
    if sum(l[i:i+m])==d:
        c+=1
print c
