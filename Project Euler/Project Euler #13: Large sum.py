n=input()
sum=0
for i in range(n):
    sum+=input()
print int(sum/(10**(len(str(sum))-10)))
