try:
	'''
	num = eval(input("Numerator:\t"))
	den = eval(input("Denominator:\t"))
	result = num/den'''
	f=open("d.txt","r")
	try:
		f.write("YO!!!!")
	finally:
		print("closes")
		f.close()
	
except ZeroDivisionError as e:
	print(e,"2")
	
except Exception as e:
	print(e,"1")
else:
	print("Executes if no exception")
'''
finally:
	print("Executes anyways")
'''