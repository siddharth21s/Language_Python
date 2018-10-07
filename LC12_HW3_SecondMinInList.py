def secmin(l):
	min,smin=l[0],l[1]
	for x in range(0,len(l)):
		if l[x] > min and l[x]<smin:
			smin=l[x]
		elif (l[x] < min) and (l[x]<smin):
			smin=min
			min=l[x]
	return [min,smin]

def main():
	x=eval(input("Enter List"))
	print(secmin(x))
	
if __name__=='__main__':
	main()