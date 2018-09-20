def multiple(x):
	if x&127==0 :
		print(x," is a multiple of 16")
	else:
		print(x," is not a multiple of 16")

x = eval(input("Enter no:\t"))
multiple(x)