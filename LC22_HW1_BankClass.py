import os
import io
import pickle
import datetime
from LC22_HW1_AccountClass import Account
from LC22_HW1_CardClass import Card

class Bank:#(Account,Card):
	AccAndCardsAssoc={}
	
	def __init__(self):
		pass
	
	def LoadFile():
		Account.LoadFile()
		Card.LoadFile()
		file = "LC22_HW1_BankClass.txt"
		f=open(file,"rb")
		Bank.AccAndCardsAssoc=pickle.load(f)
		f.close()
		
	def SaveFile():
		Account.SaveFile()
		Card.SaveFile()
		file = "LC22_HW1_BankClass.txt"
		f=open(file,"wb")
		pickle.dump(Bank.AccAndCardsAssoc,f)
		f.close()
	
	def AddAccount(self,Name,Bal,MobileNo,AadharNo):
		NewAcc = Account(Name,Bal,MobileNo,AadharNo)
		NewCard = Card()
		Bank.AccAndCardsAssoc[NewCard.CardNo] = NewAcc.AccNo
		Bank.SaveFile()
		Bank.LoadFile()
		
	def UpdateAcc(self,Field,FieldType):
		if FieldType=='Name':
			Account.UpdateName(self,Name)
			
		elif FieldType=='Mobile':
			Account.UpdateMobileNo(self,MobileNo)
		Bank.SaveFile()
		Bank.LoadFile()
		

	def AddNewCard(self):
		NewCard = Card()
		Bank.AccAndCardsAssoc[NewCard.CardNo] = self.AccNo
		Bank.SaveFile()
		Bank.LoadFile()
		
	def Deposit(self,amount):
		Account.Deposit(self,amount)
		Bank.SaveFile()
		Bank.LoadFile()
		
	def Withdraw(self,amount):
		Account.Withdraw(self,amount)
		Bank.SaveFile()
		Bank.LoadFile()
		
	def AuthCard(CardNo,Pin):
		if (CardNo in Bank.AccAndCardsAssoc) and (CardNo in Card.CardDict) :
			j = Bank.AccAndCardsAssoc[CardNo]
			CardObj = Card.CardDict[CardNo]
			if CardObj.checkValidity():
				if j in Account.Accounts:
					AccObj = Account.Accounts[j]
					if Pin == CardObj.Pin :
						return AccObj
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False
			
	
	def GetAccount():
		accNo = eval(input("Enter Account Number: "))
		if accNo in Account.Accounts:
			accObj=Account.Accounts[accNo]
			return accObj
		else:
			return False
			
	def GetCards(self):
		for i in Bank.AccAndCardsAssoc:
			if Bank.AccAndCardsAssoc[i] == self.AccNo:
				cardObj = Card.CardDict[i]
				print("Card Number: "+str(cardObj.CardNo)+"\nValidity: "+str(cardObj.Valid))

		
		
def main():
	
	Bank.LoadFile()
	print(Account.Accounts)
	print(Card.CardDict)
	print(Bank.AccAndCardsAssoc)	
	print("\t\t+BANK+")
	while True:
		ch = eval(input("\n\t+MENU+\n1.Add Account\n2.View Balance\n3.Get Cards\n4.Update Account Information\n5.Withdraw\n6.Deposit\n7.Transfer\n8.Add Card\tEnter option: "))
		if ch not in range(1,9):
			break
		elif ch == 1:
			OpenNewAccount()
		elif ch == 2:
			acn = Bank.GetAccount()
			print("Balance: ",acn.ViewBalance())
		elif ch == 3:
			acn = Bank.GetAccount()
			Bank.GetCards(acn)
		elif ch == 4:
			acn = Bank.GetAccount()
			FieldType = eval(input("Update (1)Name or (2)Mobile : "))
			Field = input("Enter value to update")
			if FieldType == 1:
				Bank.UpdateAcc(acn,Field,'Name')
			elif FieldType == 2:
				Bank.UpdateAcc(acn,Field,'Mobile')
		elif ch == 5:
			acn = Bank.GetAccount()
			amount = eval(input("Enter amount to Withdraw: "))
			Bank.Withdraw(acn,amount)
		elif ch == 6:
			acn = Bank.GetAccount()
			amount = eval(input("Enter amount to Deposit: "))
			Bank.Deposit(acn,amount)
		elif ch == 7:
			print("Enter your")
			acn1 = Bank.GetAccount()
			print("Transfer to")
			acn2 = Bank.GetAccount()
			amount = eval(input("Enter amount to Transfer: "))
			acn1.Transfer(acn2,amount)
			Bank.SaveFile()
			Bank.LoadFile()
		elif ch == 8:
			acn = Bank.GetAccount()
			Bank.AddNewCard(acn)
			
			
	'''
	bankObj = Bank()
	bankObj.AddAccount('Siddharth',500,7387838949,9890544498)
	print(Account.Accounts)
	print(Card.CardDict)
	print(Bank.AccAndCardsAssoc)
	
	accdd = Bank.AuthCard(9085543210,1234)
	print(accdd)
	accdd = Bank.AuthCard(9085543210,1334)
	print(accdd)
	Bank.SaveFile()
	
	Account.Accounts={}
	Bank.AccAndCardsAssoc={}
	Card.CardDict={}
	'''
	
def OpenNewAccount():
	bnc = Bank()
	Name = input("Enter Name: ")
	Bal = eval(input("Enter Balance : "))
	MobileNo = eval(input("Enter Mobile Number: "))
	AadharNo = eval(input("Enter AAdhar Number: "))
	bnc.AddAccount(Name,Bal,MobileNo,AadharNo)
	
if __name__=="__main__":
	main()