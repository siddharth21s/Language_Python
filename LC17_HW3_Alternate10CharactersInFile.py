import copy
import io

def parseconfig(con_fig,format='='):
	i=0
	while i!=11:
		fd= io.FileIO(con_fig)
		if fd!=None:
			
			while True:		#we can use (for line in fd) or (with open "")
				line=fd.readline()
				if line==b'':
					break
				line=str(line)
				if not (line.startswith("\\n") or line.startswith("b'#") ):	
					k=line.lstrip("b'")
					k=k.rstrip("\\r\\n\'")
					for n in range(i,len(k),10):
						print(k[n],end="\t")
		i+=1
		print()
			
		
def main():
	x=input("settings.cfg:\t")
	parseconfig(x)
	
	
	
if __name__=='__main__':
	main()