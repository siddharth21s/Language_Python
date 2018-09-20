x = input("Enter a string \t")
func(x)


def func(x):
	x=x[0]+x[1:].replace(x[0],"*")
	print(x)
