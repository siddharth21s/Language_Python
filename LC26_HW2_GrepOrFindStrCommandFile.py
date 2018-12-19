import subprocess as sp
from time import sleep
from datetime import datetime

def execu(file,commands):
	print("Executing:\t"+commands)
	print("\nCommand : findstr "+commands+" "+file+"\t"+str(datetime.now()))
	x=sp.check_call(["findstr",commands,file],shell=True)
	print("Done")
	
def main():
	file=input("Enter filename:\t")
	commands = input("Enter pattern for grep/findstr:")
	
	execu(file,commands)

if __name__=="__main__":
	main()