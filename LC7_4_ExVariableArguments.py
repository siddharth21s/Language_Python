def variable(*a):
	print(type(a))
	for x in a:
		print(x)
		
variable()
variable(1)
variable(1,2,3,4)
variable(100,20,50,40,70,10,90,101)
variable(1,"Hello",2,[1,7,11],100)