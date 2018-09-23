n=input()
l=map(int,raw_input().strip().split(' '))
l.sort()
li=[]
for i in range(5):
    li.append(l.count(i+1))
print li.index(max(li))+1
