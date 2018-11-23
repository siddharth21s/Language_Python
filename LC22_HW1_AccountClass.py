import os
import io
import pickle


class Account:
	AccountCount=100600
	Accounts = {}
	def __init__(self,Name,Bal,MobileNo,AadharNo):
		self.AccNo=Account.AccountCount
		Account.AccountCount+=1
		self.Name=Name
		self.Balance=Bal
		self.MobileNo=MobileNo
		self.AadharNo=AadharNo
		Account.Accounts[self.AccNo] = self
	
	def __repr__(self):
		return str(self.AccNo)+"\n"+str(self.Name)+"\n"+str(self.Balance)+"\n"+str(self.MobileNo)+"\n"+str(self.AadharNo)
	
	def LoadFile():
		file = "LC22_HW1_AccountClass.txt"
		f=open(file,"rb")
		Account.AccountCount=pickle.load(f)
		Account.Accounts=pickle.load(f)
		f.close()
		
	def SaveFile():
		file = "LC22_HW1_AccountClass.txt"
		f=open(file,"wb")
		pickle.dump(Account.AccountCount,f)
		pickle.dump(Account.Accounts,f)
		f.close()
		
	def ViewBalance(self):
		return self.Balance
		
	def Withdraw(self,amount):
		if (self.Balance >= amount):
			self.Balance -= amount
			return True
		else:
			return False
		
	def Deposit(self,amount):
		self.Balance += amount
		
	def Transfer(self,obj,amount):
		if isinstance(obj,Account):
			if self.Withdraw(amount):
				obj.Deposit(amount)
			else:
				return False
		else:
			self.Withdraw(amount)
	
	def UpdateName(self,Name):
		self.Name=Name
	
	def UpdateMobileNo(self,MobileNo):
		self.MobileNo=MobileNo
	
	
	
	'''def AddNewCard(self,newCard):
		pin=eval(input("Set Pin for Card: ")
		Card.setPin(newCard,pin)
		self.AssocCard[newCard.CardNo]=newCard.Pin
		Account.Accounts[self.AccNo]=self
	'''
def main():
	Account.LoadFile()
	
if __name__=='__main__':
	main()