class Account:
	accnocounter=10000
	def __init__(self,name,mobileno,aadharno,balance=0):
		self.accno= Account.accnocounter
		Account.accnocounter+=1
		self.name=name
		self.mobileno=mobileno
		self.aadharno=aadharno
		self.balance=balance
		
	def withdraw(self,money):
		if (self.balance >= money) and self.balance!=0:
			self.balance-=money
		else:
			print("Insufficient balance")
			
	def deposit(self,money):
		self.balance+=money
		
	def __repr__(self):
		return "Name: "+str(self.name)+"\nAccount No: "+str(self.accno)+"\nBalance: "+str(self.balance)+"\nMobile: "+str(self.mobileno)+"\nAadharno: "+str(self.aadharno)+"\n"
	
	def transfer(self,obj,money):
		if isinstance(obj,Account):
			if (self.balance >= money) and self.balance!=0:
				self.balance-=money
				obj.balance+=money
			else:
				print("Insufficient balance to Transfer")
		else:
			print("Error: transfer not possible")
			
			
def main():
	c=Account("Siddharth",7387838949,9890544498,500)
	print(c)
	c.withdraw(200)
	print(c)
	c.deposit(700)
	print(c)
	d=Account("Rohini",9970337780,8237146020,700)
	print(d)
	d.transfer(c,300)
	print(c)
	print(d)
	
	
if __name__=="__main__":
	main()