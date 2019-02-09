import re

def valid_email(email):
	if re.match('[\w\.-]+@[\w\.-]+(\.[\w]+)+', email):
		print('Valid Email')
	else:
		print('Invalid Email')

valid_email('shijia.hu@hcl.com')
valid_email('shijia.hu@hclcom')

