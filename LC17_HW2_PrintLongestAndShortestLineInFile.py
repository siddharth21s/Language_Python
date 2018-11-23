import copy
import io

def parseconfig(con_fig,format='='):
	rmin=''
	rmax=''
	i=0
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
				if i==0:
					rmin=copy.deepcopy(k)
				i+=1
				if len(k)>len(rmax) and i!=0:
					rmax = copy.deepcopy(k)
				if len(k)<len(rmin) and i!=0:
					rmin = copy.deepcopy(k)
		print('max->',rmax,'\nmin->',rmin)
		
		
def main():
	x=input("settings.cfg:\t")
	parseconfig(x)
	
	
	
if __name__=='__main__':
	main()