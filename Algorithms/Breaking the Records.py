n=input()
x=map(int,raw_input().split(' '))
b,w=0,0
for i in range(1,n):
    if x[i]<min(x[:i]):
        w+=1
    if x[i]>max(x[:i]):
        b+=1
print b,w         
