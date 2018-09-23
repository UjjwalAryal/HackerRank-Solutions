def leap_year(x):
    if x>1918:
        if (x%400==0)  or ((x%4==0) and (x%100!=0)):
           return 1
    elif x<1918:
        if x%4==0 :
            return 1
    return 0

y=input()
if y!=1918:
   if leap_year(y):
      print '12.09.'+str(y)
   else:
      print '13.09.'+str(y)
else:
    print '26.09.1918'
