import re
import os

def RemoveComments(x):
	#multiLine = re.compile("'''.*?'''")
	#singleLine = re.compile("#.*.")
	commentsRE = re.compile(r"(#.*.)|('''.*?''')")
	f=open(x,"r")
	Data = f.read()
	Data = re.sub(commentsRE,"",Data)
	f.close()
	x+='_comments_removed.txt'
	f=open(x,'w')
	f.write(Data)
	f.close()
	print("Done\nCheck File:",x)
	
def main():
	x=input("Enter File Name:\t")
	Exists=os.path.isfile(x)
	if Exists:
		RemoveComments(x)
	else:
		print("File does not exist")

if __name__=="__main__":
	main()