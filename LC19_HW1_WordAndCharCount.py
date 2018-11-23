import copy
import io

def parseconfig(con_fig,format='='):
	i=0
	wco=0
	cco=0
	fd= io.FileIO(con_fig)
	if fd!=None:
		
		while True:		#we can use (for line in fd) or (with open "")
			line=fd.readline()
			if line==b'':
				break
			line=str(line)
			if not (line.startswith("\\n") or line.startswith("b'#") ):	
				k=line.lstrip("b'")
				k=k.rstrip('\\r\\n\'')
				print(k)
				content=k.split(" ")
				print(content)
				print(len(content))
				wco += len(content)
				while True:
					cco+= len(content[i])
					i+=1
					if i>= len(content):
						break
				i=0
		print()
	print("word count:",wco)
	print("Char count:",cco)
		
def main():
	x=input("settings.cfg:\t")
	parseconfig(x)
	
	
	
if __name__=='__main__':
	main()