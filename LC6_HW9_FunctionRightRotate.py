x = input("Enter a 1st string \t")
y = input("Enter a 2nd string \t")
#rightrot(x,y)
def rightrot(x,y):
	u= x+x
	v = y in u
	print("2nd is right rotation of 1st: " + str(v))

rightrot(x,y)