def rightmost(p):
	return (1<<p)-1

def turnon(n,p):
	return n|rightmost(p)
	
def turnoff(n,p):
	return n&~(rightmost(p))

def toggle(n,p):
	return n^rightmost(p)
	
def main():
	n=eval(input("Enter a number:\t"))
	p=eval(input("Enter number of rightmost bits to perform action:\t"))
	a=eval(input("Action\n1:turn On\n2:turn Off\n3:Toggle\naction\t"))
	if a==1:
		print(turnon(n,p))
	elif a==2:
		print(turnoff(n,p))
	elif a==3:
		print(toggle(n,p))
	else:
		print("invalid choice")
	
	
if __name__=="__main__":
	main()