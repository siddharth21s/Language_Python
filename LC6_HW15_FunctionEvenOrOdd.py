x = eval(input("Enter no:\t"))

def check(x):
	if x&1:
		print(x," is odd")
	else:
		print(x, "is even")
		
check(x)