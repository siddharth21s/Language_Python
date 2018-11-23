import shutil
import filecmp
def archivef():
	x=input('Enter Directory path to archive as zip:\t')
	shutil.make_archive(x,'zip')
	
def copyf():
	x=input("Enter Source Name:\t")
	y=input("Enter Destination Name:\t")
	shutil.copy(x,y)

def compared():
	x=input("Enter dictoinary 1 Name and path:\t")
	y=input("Enter dictionary 2 Name and path:\t")
	z=filecmp.dircmp(x,y)
	print(z.report())
	
def main():
	i=1
	while i in range(1,3):
		i=eval(input("\n1.Archive Directory\n2.Copy file  to dest.File\n3.Compare 2 Dictionarys\nEnter valid choice"))
		if i==1:
			archivef()
		elif i==2:
			copyf()
		elif(i==3):
			compared()
if __name__ == "__main__":
    main()
