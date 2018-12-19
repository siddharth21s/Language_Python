def  addout(num):
	def addin(numb):
		return num+numb
	return  addin
	
def main():
	add10 = addout(10)
	add100 = addout(100)
	print(type(add10))
	print(type(add100))
	print(add10(90))
	print(add100(90))
	
if __name__=="__main__":
	main()