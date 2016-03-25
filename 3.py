loginid=raw_input("Enter ID please :")
words=["alice","bob","john","peter"]
if(loginid in words):
	print loginid+" " +"you have successfully logged in"
else:
	print 'sorry,unknown user try again'
