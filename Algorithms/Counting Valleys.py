n = int (raw_input())
valley,level = 0,0
flag =False
for step in raw_input():
	if level==0:
		flag = True
	if step=='D':
		level-=1
	else:
		if level<0 and flag:
			flag = False
			valley+=1
		level+=1
print valley
