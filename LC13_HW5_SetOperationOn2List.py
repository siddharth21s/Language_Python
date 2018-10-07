def unionr(x,y):
	z=[]
	i,j=0,0
	while(i < len(x)):
		if(x[i] in y):
			z.append(x[i])
		i+=1
	i,j=0,0
	while(i<len(x)):
		if(x[i] not in z):
			z.append(x[i])
		i+=1
	while(j<len(y)):
		if(y[j] not in z):
			z.append(y[j])
		j+=1
	z.sort()
	print("\nUnion :",z,"\n")
	return

	
def intersec(x,y):
	z=[]
	i,j=0,0
	while(i < len(x)):
		if(x[i] in y):
			z.append(x[i])
		i+=1
	print("\nIntersection :",z,"\n")
	return

	
def diff(x,y):
	z=[]
	i,j=0,0
	while(i < len(x)):
		if(x[i] not in y):
			z.append(x[i])
		i+=1
	print("\nDiff :",z,"\n")
	return


def symdiff(x,y):
	z=[]
	i=0
	while(i < len(x)):
		if(x[i] not in y):
			z.append(x[i])
		i+=1
	i=0
	while(i < len(y)):
		if(y[i] not in x):
			z.append(y[i])
		i+=1
	z.sort()
	print("\nSymdiff :",z,"\n")

	
def main():
	print("Enter 1st list Elements")
	x=[int(a) for a in input().split()]
	print("Enter 2nd list Elements")
	y=[int(a) for a in input().split()]
	x.sort()
	y.sort()
	c = '2'
	while (c in "1UnionUNIONunion2INTERSECIntersecintersec3DIFFdiffDiff4SYMDIFFsymdiffSymdiff"):
		c=input("1.Union\n2.Intersec\n3.Diff\n4.Symdiff\nchoice:\t")
		if(c in "1UnionUNIONunion"):
			unionr(x,y)
		elif(c in "2INTERSECIntersecintersec"):
			intersec(x,y)
		elif(c in "3DIFFdiffDiff"):
			d=eval(input("Enter 1 for x-y and 2 for y-x:\t"))
			if(d==1):
				diff(x,y)
			else:
				diff(y,x)
		elif(c in "4SYMDIFFsymdiffSymdiff"):
			symdiff(x,y)
	
if __name__=='__main__':
	main()