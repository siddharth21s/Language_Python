l = eval(input("Enter lower no:\t"))
u = eval(input("Enter upper no:\t"))

while l<=u:
	if (l%5)==0:
		print(l)
	else:
		pass
	l+=1


# done is not executed when jump statement is used: break
'''
for x in range(l,u+1,2):
	print(x)
	if (x%48)==0:
		break
	print(x*x)
else:
	print("Done")
	'''
#done is executed even when jump statement is used ie: continue	
'''
for x in range(l,u+1,):
	print(x)
	if (x%4)==0:
		continue
	print(x*x)
else:
	print("Done")