import re

def valid_ip_address(ip):
	if re.match('((25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\.){3}(25[0-5]|2[0-4]\\d|[01]?\\d\\d?)', ip):
		print('Valid IP address')
	else:
		print('Invalid IP address')

valid_ip_address('256.2.2.2')
valid_ip_address('123.33.3.3')
