import os
import io
import pickle

#LC22_HW2_BookClass.py

class :
	BookCount=100600
	Books = {}
	def __init__(self,Name,Author):
		self.BookNo=Book.BookCount
		Book.BookCount+=1
		self.Name=Name
		self.Author=Author
		self.BookOnShelf = True
		Book.Books[self.BookNo] = self
	
	def __repr__(self):
		return str(self.BookNo)+"\n"+str(self.Name)+"\n"+str(self.Author)#+"\n"+str(self.BookLimit)
	
	def LoadFile():
		file = "LC22_HW1_BookClass.txt"
		f=open(file,"rb")
		Book.BookCount=pickle.load(f)
		Book.Books=pickle.load(f)
		f.close()
		'''
	def SaveFile():
		file = "LC22_HW1_BookClass.txt"
		f=open(file,"wb")
		pickle.dump(Book.BookCount,f)
		pickle.dump(Book.Books,f)
		f.close()
		
	def ViewAuthor(self):
		return self.Author
		
	def Withdraw(self,amount):
		if (self.Author >= amount):
			self.Author -= amount
			return True
		else:
			return False
		
	def Deposit(self,amount):
		self.Author += amount
		
	def Transfer(self,obj,amount):
		if isinstance(obj,Book):
			if self.Withdraw(amount):
				obj.Deposit(amount)
			else:
				return False
		else:
			self.Withdraw(amount)
		'''
	def UpdateName(self,Name):
		self.Name=Name
	
	def UpdateAuthor(self,Author):
		self.Author=Author
	
	
	
	'''def AddNewCard(self,newCard):
		pin=eval(input("Set Pin for Card: ")
		Card.setPin(newCard,pin)
		self.AssocCard[newCard.CardNo]=newCard.Pin
		Book.Books[self.BookNo]=self
	'''
def main():
	Book.LoadFile()
	
if __name__=='__main__':
	main()