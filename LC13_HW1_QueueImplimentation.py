def push(y,d):
	if(isfull(y)==1):
		return y.append(d)
	#del can be used to delete element in list

def popp(y):
	if(isempty(y)==1):
		p=y.pop(peep(y))
		print(p)
		return y
	
def isempty(y):
	if len(y)<=100 and len(y)>0:
		return 1
	print("Queue Empty")
	return 0

def isfull(y):
	if len(y)==100:
		print("Queue full")
		return 0
	return 1
def peep(y):
	if(isempty(y)==1):
		print("Front:\t",y[0])
	return 0
	
def main():
	print("Enter Queue Elements")
	y=[int(a) for a in input().split()]
	while True:
		c=input("1.push\n2.pop\n3.peep\n4.exit\n input valid choice\t")
		if(c in "1PushpushPUSH"):
			d=eval(input("Enter data\t"))
			push(y,d)
		
		elif(c in "2PopPOPpop"):
			popp(y)
		
		elif(c in "3PeepPEEPpeep"):
			peep(y)
		elif(c in "4ExitexitEXIT"):
			break

if __name__=='__main__':
	main()
	