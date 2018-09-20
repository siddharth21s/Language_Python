x=eval(input("Enter no1\t"))

def donuts(x):
	if x<0:
		print("not even tried donuts :D")
	elif x>=0 and x<=2:
		print("too few donuts")
	elif x<=10:
		print("donuts:" ,x)
	else:
		print("so many donuts")
donuts(x)