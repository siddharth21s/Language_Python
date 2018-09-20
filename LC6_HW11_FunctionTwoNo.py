x=eval(input("Enter no1\t"))
y=eval(input("Enter no2\t"))

def func(x,y):
	if x>y:
		print(x-y)
	elif x==y:
		print(x,y)
	else:
		print(x+y)

func(x,y)