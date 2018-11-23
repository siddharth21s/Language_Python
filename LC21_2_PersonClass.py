class Person:
	def __init__(self,name,address,mobileno,aadharno,gender):
		self.name=name
		self.address=address
		self.mobileno=mobileno
		self.aadharno=aadharno
		self.gender=gender
	
	def __repr__(self):
		return "\nName: "+str(self.name)+"\nAddress: "+str(self.address)+"\nMobile No: "+str(self.mobileno)+"\nAadhar No: "+str(self.aadharno)+"\nGender: "+str(self.gender)
	
	def updatename(self,name):
		self.name=name
		
	def updateaddress(self,addr):
		self.address=addr
		
	def updatemobile(self,mobileno):
		self.mobileno=mobileno
	
def main():
	a=Person('Siddharth','168, MG road',7387838949,9890544498,'Male')
	print(a)
	a.updatename('Siddharth Sadaphule')
	a.updateaddress("168 MG Road, Pune")
	a.updatemobile(9970337780)
	print(a)

if __name__=='__main__':
	main()