import os
import io
import pickle
import datetime
from LC22_HW1_BankClass import Bank

class ATM(Bank):
	def __init__(self,cardNum,Pin):
		self.CardNo = cardNum
		self.Pin=Pin
		self.AccObj = Bank.AuthCard(self.CardNo,self.Pin)
			
	def One(self,amount):
		d = self.AccObj
		d.Withdraw(amount)
			
	def Two(self,amount):
		d = self.AccObj
		d.Deposit(amount)
	
	def Three(self):
		d = self.AccObj
		return d.Balance

	
def main():
	Bank.LoadFile()
	cardNum=eval(input("\t\t+ATM+\nSwipe card: "))
	Pin=eval(input("Enter pin: "))
	
	while True:
		
		ATMObj = ATM(cardNum,Pin)
		if ATMObj.AccObj == False:
			print("++++++++Invalid Card or Pin++++++++")
			break
		else:
			ch=eval(input("\n\t+MENU+\n1.Withdraw\n2.Deposit\n3.View Balance\n4.Exit\tEnter option: "))
			if ch == 4:
				break
			elif ch == 1:
				amount=eval(input("Enter Amount to Withdraw: "))
				ATMObj.One(amount)
				bal = ATMObj.Three()
				print("Balnce in Account: ",bal)
				Bank.SaveFile()	
			elif ch == 2:
				amount=eval(input("Enter Amount to Deposit: "))
				ATMObj.Two(amount)
				bal = ATMObj.Three()
				print("Balnce in Account: ",bal)
				Bank.SaveFile()	
			elif ch == 3:
				bal = ATMObj.Three()
				print("Balnce in Account: ",bal)
				Bank.SaveFile()	
			
				
if __name__=="__main__":
	main()