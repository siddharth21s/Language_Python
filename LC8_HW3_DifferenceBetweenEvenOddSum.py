def esum(n,e):
	if n==0:
		return 0
	elif((n%10)%2==0):
		e=n%10+esum(int(n/10),e)
		return e
	else:
		e=0+esum(int(n/10),e)
		return e

def osum(n,o):
	if n==0:
		return 0
	elif((n%10)%2!=0):
		o=n%10+osum(int(n/10),o)
		return o
	else:
		o=0+osum(int(n/10),o)
		return o

def main():
	n=eval(input("Enter Digit\t"))
	e = esum(n,0)
	o = osum(n,0)
	print("Even Sum:",e,"Odd Sum:",o,"\nEvensum-Oddsum :",e-o)
	

	
if __name__=='__main__':
	main()
	