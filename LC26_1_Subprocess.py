import subprocess as sp
from time import sleep

def outlist(timer,iteration):
	for i in range(0,iteration):
		x=sp.check_call("TASKLIST",shell=True)
		print("*******",i,"*******")
		print(x)
		print()
		sleep(timer)
		
def main():
	timer=eval(input("Enter Time Interval:\t"))
	iteration = eval(input("Enter No of Iterations:\t"))
	outlist(timer,iteration)

if __name__=="__main__":
	main()