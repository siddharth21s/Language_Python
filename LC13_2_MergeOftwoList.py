def third(x,y):
	z=[]
	i,j=0,0
	while True:
		if i == len(x):
			z.extend(y[j:])
			break
		elif j == len(y):
			z.extend(x[i:])
			break
		elif x[i] < y[j]:
			z.append(x[i])
			i+=1
		elif x[i] > y[j]:
			z.append(y[j])
			j+=1
	return z
	
	
def main():
	print("Enter 1st list Elements")
	x=[int(a) for a in input().split()]
	print("Enter 2nd list Elements")
	y=[int(a) for a in input().split()]
	x.sort()
	y.sort()
	print(third(x,y))
	
if __name__=='__main__':
	main()