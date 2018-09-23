l=list(raw_input())
if l[8]=='P' and int(l[0]+l[1])!=12:
   h=12+int(l[0]+l[1])
elif l[8]=='A' and int(l[0]+l[1])==12:
    h=0
else:
    h=int(l[0]+l[1])
if h>9:
    print str(h)+':'+''.join(l[3:5])+':'+''.join(l[6:8])
else:
    print '0'+str(h)+':'+''.join(l[3:5])+':'+''.join(l[6:8]) 
