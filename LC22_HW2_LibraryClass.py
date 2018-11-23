import os
import io
import pickle
import datetime
from LC22_HW1_BookClass import Book
from LC22_HW1_LibCardClass import LibCard

class Library(Book,LibCard):
	BookAndLibCardsAssoc={}
	
	def __init__(self):
		pass
	
	def LoadFile():
		Book.LoadFile()
		LibCard.LoadFile()
		file = "LC22_HW1_LibraryClass.txt"
		f=open(file,"rb")
		Library.BookAndLibCardsAssoc=pickle.load(f)
		f.close()
		
	def SaveFile():
		Book.SaveFile()
		LibCard.SaveFile()
		file = "LC22_HW1_LibraryClass.txt"
		f=open(file,"wb")
		pickle.dump(Library.BookAndLibCardsAssoc,f)
		f.close()
	
	def AddBook(self,Name,Author):
		Book(Name,Author)
		Library.SaveFile()
		Library.LoadFile()
		
	def UpdateBook(self,Field,FieldType):
		if FieldType=='Name':
			Book.UpdateName(self,Name)
			
		elif FieldType=='Author':
			Book.UpdateMobileNo(self,Author)
		Library.SaveFile()
		Library.LoadFile()
		

	def AddNewLibCard(self):
		NewLibCard = LibCard()
		Library.BookAndLibCardsAssoc[NewLibCard.LibCardNo] = self.BookNo
		Library.SaveFile()
		Library.LoadFile()
		
	def AuthLibCard(LibCardNo):
		if (LibCardNo in Library.BookAndLibCardsAssoc) and (LibCardNo in LibCard.LibCardDict) :
			j = Library.BookAndLibCardsAssoc[LibCardNo]
			LibCardObj = LibCard.LibCardDict[LibCardNo]
			if LibCardObj.checkValidity():
				if j in Book.Books:
					BookObj = Book.Books[j]
					return BookObj
				else:
					return False
			else:
				return False
		else:
			return False
			
	
	def GetBook():
		BookNo = eval(input("Enter Book Number: "))
		if BookNo in Book.Books:
			BookObj=Book.Books[BookNo]
			return BookObj
		else:
			return False
			
	def GetLibCards(self):
		for i in Library.BookAndLibCardsAssoc:
			if Library.BookAndLibCardsAssoc[i] == self.BookNo:
				LibCardObj = LibCard.LibCardDict[i]
				print("LibCard Number: "+str(LibCardObj.LibCardNo)+"\nValidity: "+str(LibCardObj.Valid))

		
		
def main():
	
	Library.LoadFile()
	print(Book.Books)
	print(LibCard.LibCardDict)
	print(Library.BookAndLibCardsAssoc)	
	print("\t\t+Library+")
	while True:
		ch = eval(input("\n\t+MENU+\n1.Add Book\n2.View Balance\n3.Get LibCards\n4.Update Book Information\n5.Withdraw\n6.Deposit\n7.Transfer\n8.Add LibCard\tEnter option: "))
		if ch not in range(1,9):
			break
		elif ch == 1:
			OpenNewBook()
		elif ch == 2:
			acn = Library.GetBook()
			print("Balance: ",acn.ViewBalance())
		elif ch == 3:
			acn = Library.GetBook()
			Library.GetLibCards(acn)
		elif ch == 4:
			acn = Library.GetBook()
			FieldType = eval(input("Update (1)Name or (2)Mobile : "))
			Field = input("Enter value to update")
			if FieldType == 1:
				Library.UpdateBook(acn,Field,'Name')
			elif FieldType == 2:
				Library.UpdateBook(acn,Field,'Mobile')
		elif ch == 5:
			acn = Library.GetBook()
			amount = eval(input("Enter amount to Withdraw: "))
			Library.Withdraw(acn,amount)
		elif ch == 6:
			acn = Library.GetBook()
			amount = eval(input("Enter amount to Deposit: "))
			Library.Deposit(acn,amount)
		elif ch == 7:
			print("Enter your")
			acn1 = Library.GetBook()
			print("Transfer to")
			acn2 = Library.GetBook()
			amount = eval(input("Enter amount to Transfer: "))
			acn1.Transfer(acn2,amount)
			Library.SaveFile()
			Library.LoadFile()
		elif ch == 8:
			acn = Library.GetBook()
			Library.AddNewLibCard(acn)
			
			
	'''
	LibraryObj = Library()
	LibraryObj.AddBook('Siddharth',500,7387838949,9890544498)
	print(Book.Books)
	print(LibCard.LibCardDict)
	print(Library.BookAndLibCardsAssoc)
	
	Bookdd = Library.AuthLibCard(9085543210,1234)
	print(Bookdd)
	Bookdd = Library.AuthLibCard(9085543210,1334)
	print(Bookdd)
	Library.SaveFile()
	
	Book.Books={}
	Library.BookAndLibCardsAssoc={}
	LibCard.LibCardDict={}
	'''
	
def OpenNewBook():
	bnc = Library()
	Name = input("Enter Name: ")
	Bal = eval(input("Enter Balance : "))
	MobileNo = eval(input("Enter Mobile Number: "))
	AadharNo = eval(input("Enter AAdhar Number: "))
	bnc.AddBook(Name,Bal,MobileNo,AadharNo)
	
if __name__=="__main__":
	main()