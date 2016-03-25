class Employee:
	

	def __init__(self, name):
   		self._name = name
   		

	def get_name(self):
		return self._name


e = Employee("zaid")
print e.get_name()
