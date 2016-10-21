# Israel O. Dilan-Pantojas
# israel.dilan@upr.edu
# Code 2040 
# Step 4
import requests
import json

# Initialize Dictionary
data = {'token':'c13b0b5d48c020b2804774cf748765f7'}

# Request string from API endpoint
r = requests.post('http://challenge.code2040.org/api/prefix', json = data)

# Review API response
print r.status_code
if (r.status_code != 200):
	print ("Something weird with status code " + r.status_code + "is going on.")
else:
	print r.text

# Converts JSON formatted string to python dictionary 
dictionary = json.loads(r.text)

# Separate prefix from Dictionary
prefix = dictionary['prefix']

# Separate the array from Dictionary
array = dictionary['array']



# Look for strings prefixed by prefix and avoid adding them to clean array
clean = []
for i in array:
	if (i.startswith(prefix, 0)):
		pass
	else:		
		clean.append(i)

# Review data in dictionary 
data['array'] = clean

# Validate result
r2 = requests.post('http://challenge.code2040.org/api/prefix/validate', json = data)

# Review API validation response
print r2.status_code
if (r2.status_code != 200):
	print ("Something weird with status code " + r2.status_code + "is going on.")
else:
	print r2.text