# Israel O. Dilan-Pantojas
# israel.dilan@upr.edu
# Code 2040 
# Step 3
import requests
import json

# Initialize Dictionary
data = {'token':'c13b0b5d48c020b2804774cf748765f7'}

# Request string from API endpoint
r = requests.post('http://challenge.code2040.org/api/haystack', json = data)

# Review API response
print r.status_code
if (r.status_code != 200):
	print ("Something weird with status code " + r.status_code + "is going on.")
else:
	print r.text

# Converts JSON formatted string to python dictionary 
dictionary = json.loads(r.text)

# Separate needle from Dictionary
needle = dictionary['needle']

# Separate the haystack from Dictionary
haystack = dictionary['haystack']

# Look for needle in haystack and return position 
pos = haystack.index(needle) 

# Review data in dictionary 
data['needle'] = pos

# Validate result
r2 = requests.post('http://challenge.code2040.org/api/haystack/validate', json = data)

# Review API validation response
print r2.status_code
if (r2.status_code != 200):
	print ("Something weird with status code " + r2.status_code + "is going on.")
else:
	print r2.text