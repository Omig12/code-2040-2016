# Israel O. Dilan-Pantojas
# israel.dilan@upr.edu
# Code 2040 
# Step 2

import requests

# Initialize Dictionary
data = {'token':'c13b0b5d48c020b2804774cf748765f7'}

# Request string from API endpoint
r = requests.post('http://challenge.code2040.org/api/reverse', json = data)

# Review API response
print r.status_code
if (r.status_code != 200):
	print ("Something weird with status code " + r.status_code + "is going on.")
else:
	print r.text

# Reverse string and store it in dicitonary
data['string'] = r.text[::-1]
 
# Review data in dictionary
print data

# Validate result
r2 = requests.post('http://challenge.code2040.org/api/reverse/validate', json = data)

# Review API validation response
print r2.status_code
if (r2.status_code != 200):
	print ("Something weird with status code " + r2.status_code + "is going on.")
else:
	print r2.text