def fib_seq(num):
	n1 = 0
	n2 = 1
	count = 0
	fib_list = []
	if num == 1:
		return n1
	elif num >= 2:
		while count < num:
			fib_list.append(str(n1))
			n = n1 + n2
			n1 = n2
			n2 = n
			count += 1
	return ','.join(fib_list)

print(fib_seq(10))
