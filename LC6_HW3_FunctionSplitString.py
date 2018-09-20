def stringsplit():
	s = input("Enter string :\t")
	x = eval(input("Enter start index :\t"))
	y = eval(input("Enter end  index :\t"))
	z = eval(input("Enter step value :\t"))
	print(s[x:y:z])
	
stringsplit()