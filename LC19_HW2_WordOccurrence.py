import copy
import io

def parseconfig(con_fig,w,con):
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
				content=k.split(" ")
				if content.count(w) == con:
					print(k)
		print()
		
def main():
	x=input("settings.cfg:\t")
	print("Enter Word")
	w=input("")
	con=eval(input("Enter the occurrence\n"))
	parseconfig(x,w,con)
	
	
	
if __name__=='__main__':
	main()