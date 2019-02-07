
def check_num_vaild(func):
	def func_wrapper(x, y):
		if type(x) not in (int, float) or type(y) not in (int, float):
			raise Exception("Both x and y have to be valid number for function {} to work".format(func.__name__))
		res = func(x, y)
		return res
	return func_wrapper

@check_num_vaild
def addition(x, y):
	return x + y

print(addition(1,2))
print(addition(1,'2'))