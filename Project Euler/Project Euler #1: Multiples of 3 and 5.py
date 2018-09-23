t = int(input().strip())
for a0 in range(t+1):
    n = int(input().strip())
    n1,n2,n3=(n-1)//3,(n-1)//5,(n-1)//15
    print (int((n1*(3*n1+3)  +  n2*(5*n2+5)  -   n3*(15*n3+15))>>1))
