n = input()
a = map(int,raw_input().strip().split(' '))
ma = 0
for i in set(a):
    ma = max(ma, a.count(i-1)+a.count(i) , a.count(i+1)+a.count(i))
print ma    
