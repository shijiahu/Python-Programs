import re

def valid_phone_number(phone):
	if re.match(r'(\+1)*\s?[0-9]{3}\s?[0-9]{3}\s?[0-9]{4}', phone):
		print('Valid number')
	else:
		print('Invalid number')

valid_phone_number('+1 234 567 2345')