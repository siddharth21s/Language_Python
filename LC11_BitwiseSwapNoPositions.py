def gno(p,b):
	return (((1<<b)-1)<<(p-b))

def swapno(n1,n2,p,b):
	r1=n1&gno(p,b)
	r2=n2&gno(p,b)
	n1=n1&~(gno(p,b))
	n2=n2&~(gno(p,b))
	n1=n1|r2
	n2=n2|r1
	print(n1,n2)
	
def main():
	x=eval(input("Enter no1:\t"))
	y=eval(input("Enter no2:\t"))
	z=eval(input("Enter position:\t"))
	w=eval(input("Enter no of bits from the given postion"))
	if w>z:
		w=z
	print("Result:")
	swapno(x,y,z,w)
	
if __name__=="__main__":
	main()