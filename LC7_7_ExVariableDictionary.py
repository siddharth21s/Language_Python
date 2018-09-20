def check(*b,**d):
	print(type(b))
	print(type(d))
	for x in b:
		print(x)
	for x in d:
		print(x,d[x])
	
check(1,2,name="siddharth",hobby="basketball",age=22)
