import copy
import io

def parseconfig(con_fig,w):
	i=0
	f=0
	res=''
	fd= io.FileIO(con_fig)
	if fd!=None:
		
		while True:		#we can use (for line in fd) or (with open "")
			line=fd.read()
			if line==b'':
				break
			line=str(line)
			if not (line.startswith("\\n") or line.startswith("b'#") ):	
				k=line.lstrip("b'")
				k=k.rstrip('\\r\\n\'')
				
				content=k.split(". ")
				while i<len(content):
					content[i]=content[i].replace('\\r\\n',' ')
					if w in content[i]:
						print(content[i])
					i+=1
				
		print()
		
def main():
	x=input("settings.cfg:\t")
	print("Enter Word")
	w=input("")
	parseconfig(x,w)
	
	
	
if __name__=='__main__':
	main()