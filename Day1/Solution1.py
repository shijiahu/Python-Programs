def dec_to_bin(num):
	binary_list = []
	while num > 0:
		binary_list.append(str(num % 2))
		num = num // 2
	result = ''.join(binary_list[::-1])
	return result

print(dec_to_bin(16))
