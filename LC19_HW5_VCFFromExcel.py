import copy
import io
import vcard
import xlrd
def parseconfig(x):
	i=0
	f=0
	res=''
	f=open("LC19_HW5.vcf","w")
	f1= xlrd.open_workbook(x)
	sh=f1.sheet_by_index(0)
	sh.cell_value(1,0)
	for q in range(1,sh.nrows):
		l=sh.row_values(q)
		print(l)
		f.write( 'BEGIN:VCARD' + "\n")
		f.write( 'VERSION:3.0' + "\n")
		f.write( 'N:' + l[0] + "\n")
		f.write( 'TEL;CELL:' + l[1] + "\n")
		f.write( 'EMAIL:' + str(int(l[2])) + "\n")
		f.write( 'END:VCARD' + "\n")
		f.write( "\n")
		print()
	f.close()
	
def main():
	x=input("LC19_HW5.xlsx:\t")
	parseconfig(x)
	
	
	
if __name__=='__main__':
	main()