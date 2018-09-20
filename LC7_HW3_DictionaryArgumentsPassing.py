def check(*b,**d):
	print(type(b))
	print(type(d))
	for x in b:
		print(x)
	for x in d:
		print(x,d[x])
	print(b)
	print(d)

x,y=eval(input("Enter two Numbers"))
details = input("Enter in format of dictionary")# not  considered as key value pair when passed in function
print(details)
check(x,y,details)
