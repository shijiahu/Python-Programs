class Calculator():
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	def add(self):
		return self.num1 + self.num2
	def sub(self):
		return self.num1 - self.num2
	def mul(self):
		return self.num1 * self.num2
	def div(self):
		return self.num1 / self.num2

if __name__=='__main__':
    my_calculator = Calculator(2,3)
    print(my_calculator.add())
    print(my_calculator.sub())
    print(my_calculator.mul())
    print(my_calculator.div())
