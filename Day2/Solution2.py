# parent class
class Calculator_Input(object):
	def __init__(self):
		while True:
			try:
				self.num1 = float(input('Enter your first number:'))
				self.num2 = float(input('Enter your second number:'))
				break
			except:
				print('Please input valid number!')
		
class Calculator(Calculator_Input):
	def add(self):
		return self.num1 + self.num2
	def sub(self):
		return self.num1 - self.num2
	def mul(self):
		return self.num1 * self.num2
	def div(self):
		return self.num1 / self.num2

if __name__=='__main__':
    my_calculator = Calculator()
    print(my_calculator.add())
    print(my_calculator.sub())
    print(my_calculator.mul())
    print(my_calculator.div())
