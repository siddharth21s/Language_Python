x=eval(input("Enter no1\t"))
y=eval(input("Enter no2\t"))
z=eval(input("Enter no3\t"))
def minof(x,y,z):
	if x<y and x<z:
		print("min :" ,x)
	elif y<z:
		print("min :" ,y)
	else:
		print("min :" ,z)
minof(x,y,z)