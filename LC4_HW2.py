x = input("Enter a string \t")
x=x[0]+x[1:].replace(x[0],"*")
print(x)

'''
>>> x.replace("a","s")
'ssssss'
>>> x.replace("s","*")
'a*a*a*'
>>> x
'asasas'
>>> x.replace("x[0]","*")
'asasas'
>>> y=x.replace("a","*")
>>> y
'*s*s*s'
>>> x = input("Enter a string \t")
Enter a string  y=x[0]
>>> y=x[1:].replace(y,"*")
>>> print(y)
=x[0]
>>>
>>>
>>> x = input("Enter a string \t")
Enter a string  asdasdasdasd
>>> y=x[0]
>>> y
'a'
>>> y=x[1:].replace(y,"*")
>>> y
'sd*sd*sd*sd'
>>> x
'asdasdasdasd'
>>> y=x[0] + x[1:].replace(x[0],"*")
>>> y
'asd*sd*sd*sd'
>>>'''