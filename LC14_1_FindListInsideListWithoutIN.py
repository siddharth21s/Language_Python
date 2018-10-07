def main():
	print("Enter 1st list Elements")
	x=eval(input(""))
	print("x: ",x)
	print("Enter 2nd list Elements")
	y=eval(input(""))
	print("y: ",y)
	z=[]
	z=checklist(x,y,z)
	print("Result: ",z)
	
def checklist(x,y,z):
	s=set(x)
	t=set(y)
	r=t.issubset(s)
	#print(r)
	return r


if __name__=='__main__':
	main()