x=raw_input("Enter String :")
y=raw_input("Enter String 2:")
print x.upper()
print y.lower()
	
if(len(x) == len(y)):
	print 'Strings are the same length'
	if(x == y):
		print 'Strings have the same content'
	
	else:
		print 'Strings have different content'
else:
	print 'Strings are a different length'

	

