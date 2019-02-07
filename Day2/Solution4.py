import re, os
path = "/Users/shijiahu/Desktop/test"
for root, dirs, files in os.walk(path):
    for file in files:
    	if re.search(r'hcl', file, re.IGNORECASE):
        	print(file)
    for dir in dirs:
    	if re.search(r'hcl', dir, re.IGNORECASE):
    		print(dir)
