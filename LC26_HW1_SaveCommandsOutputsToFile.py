import subprocess as sp
from time import sleep
from datetime import datetime

def execu(file,commands):
	f=open(file,"w")
	
	for i in commands:
		x=sp.getoutput(i)
		print("Executing:\t"+i)
		c="\nCommand :"+i+"\t"+str(datetime.now())
		f.write(c)
		f.write(x)
	
	f.close()
	print("Done")
	
def main():
	file=input("Enter filename:\t")
	commands = []
	print("Enter commands | Enter 'end' to stop:")
	while True:
		x=input("Command:\t")
		if x in "ENDendEnd":
			break
		else:
			commands.append(x)
	execu(file,commands)

if __name__=="__main__":
	main()