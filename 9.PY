class BMI:
    def __init__(height,weight):
        self.height = height
        self.weight = weight
	
    def myBMI(self):
        return (self.weight*703/self.height)
    
A = BMI(10,10)
print A.myBMI()

