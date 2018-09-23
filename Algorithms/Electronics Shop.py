s,n,m=map(int,raw_input().strip().split(' '))
k=map(int,raw_input().strip().split(' '))
u=map(int,raw_input().strip().split(' '))
max=-1
for i in k:
    for j in u:
        if (i+j)==s:
            print s
            exit()
        elif (i+j)<=s:
            if max<(i+j):
                max=i+j

print max

            
