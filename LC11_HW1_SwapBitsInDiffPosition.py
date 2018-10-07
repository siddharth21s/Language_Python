def  swapbits(n1,n2,p1,p2,b):
	m1 = ((n1 & (( ( (1<<b)-1) ) << (p1-b) )) >> (p1-b))<<(p2-b)
	m2 = ((n2 & (( ((1<<b)-1))<<(p2-b) ))>>(p2-b))<<(p1-b)
	n1 = n1 & ~(( ((1<<b)-1))<<(p1-b))
	n2 = n2 & ~(( ((1<<b)-1))<<(p2-b))
	
	print("Result:\n n1: ",n1|m2,"\n n2: ",n2|m1)

def main():
	x=eval(input("Enter n1:\t"))
	y=eval(input("Enter n2:\t"))
	z=eval(input("Enter Position of bits in n1:\t"))
	u=eval(input("Enter Position of bits in n2:\t"))
	v=eval(input("Enter no of bits:\t"))
	if (z-v)<0:
		v=z
	elif (u-v)<0:
		v=u
	swapbits(x,y,z,u,v)

if __name__=='__main__':
	main()