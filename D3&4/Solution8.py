def increase_ip(ip_address, num):
	ip_address_list = ip_address.split('.')
	for i in range(len(ip_address_list)):
		ip_address_list[i] = int(ip_address_list[i])
	result = ip_address_list
	carry = (result[-1] + num)//255
	rest = (result[-1] + num)%255
	result[-1] = rest
	for i in range(2,len(result)+1):
		temp = result[-i] + carry
		carry = temp//255
		rest = temp%255
		result[-i] = rest
	print('.'.join(str(x) for x in result))

increase_ip('192.168.3.225', 100)