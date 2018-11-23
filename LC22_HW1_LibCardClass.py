import os
import io
import pickle
import datetime

#LC22_HW1_LibCardClass.py

class LibCard:
	LibCardNoCount=9085543210
	LibCardDict={}
	def __init__(self,Name,Bal,MobileNo):
		self.LibCardNo=LibCard.LibCardNoCount
		LibCard.LibCardNoCount+=1
		self.Name=Name
		self.Balance=Bal
		self.MobileNo=MobileNo
		LibCard.LibCardDict[self.LibCardNo]=self
	
	def LoadFile():
		file = "LC22_HW1_LibCardClass.txt"
		f=open(file,"rb")
		LibCard.LibCardNoCount=pickle.load(f)
		LibCard.LibCardDict=pickle.load(f)
		f.close()
		
	def SaveFile():
		file = "LC22_HW1_LibCardClass.txt"
		f=open(file,"wb")
		pickle.dump(LibCard.LibCardNoCount,f)
		pickle.dump(LibCard.LibCardDict,f)
		f.close()
		
	def getLibCard(self):
		return self.LibCardno
	
	def getPin(self):
		return self.Pin
		
	def setPin(self,Pin):
		self.Pin=Pin
		LibCard.LibCardDict[self.LibCardNo]=self.Pin
		
	def checkValidity(self):
		now = datetime.datetime.now()
		if self.Valid >= now:
			return True
		else:
			return False
	
	def __repr__(self):
		return "\nLibCard No: "+str(self.LibCardNo)+"\nType: "+str(self.Type)+"\nValidity:"+str(self.Valid)
	
def main():
	vLibCard = LibCard()
	print(vLibCard)
	
	
if __name__=='__main__':
	main()
	
	