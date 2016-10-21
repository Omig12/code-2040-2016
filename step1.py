# Israel O. Dilan-Pantojas
# israel.dilan@gmail.com
# Code 2040 
# Step 1

import requests

# Initialize Dictionary
data = {'token':'c13b0b5d48c020b2804774cf748765f7', 'github':'https://github.com/Omig12/code-2040-2016'}

# Send data to API endpoint
r = requests.post('http://challenge.code2040.org/api/register', json = data)

# Review API response
print r.status_code
if (r.status_code != 200):
	print ("Something weird with status code " + r.status_code + "is going on.")
else:
	print r.text