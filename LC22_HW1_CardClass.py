import os
import io
import pickle
import datetime

class Card:
	CardNoCount=9085543210
	CardDict={}
	def __init__(self):
		self.CardNo=Card.CardNoCount
		Card.CardNoCount+=1
		self.Type='Visa'
		self.Pin=1234#None
		self.Valid=datetime.datetime.now()+datetime.timedelta(days=365*10)
		Card.CardDict[self.CardNo]=self
	
	def LoadFile():
		file = "LC22_HW1_CardClass.txt"
		f=open(file,"rb")
		Card.CardNoCount=pickle.load(f)
		Card.CardDict=pickle.load(f)
		f.close()
		
	def SaveFile():
		file = "LC22_HW1_CardClass.txt"
		f=open(file,"wb")
		pickle.dump(Card.CardNoCount,f)
		pickle.dump(Card.CardDict,f)
		f.close()
		
	def getCard(self):
		return self.Cardno
	
	def getPin(self):
		return self.Pin
		
	def setPin(self,Pin):
		self.Pin=Pin
		Card.CardDict[self.CardNo]=self.Pin
		
	def checkValidity(self):
		now = datetime.datetime.now()
		if self.Valid >= now:
			return True
		else:
			return False
	
	def __repr__(self):
		return "\nCard No: "+str(self.CardNo)+"\nType: "+str(self.Type)+"\nValidity:"+str(self.Valid)
	
def main():
	vCard = Card()
	print(vCard)
	
	
if __name__=='__main__':
	main()
	
	