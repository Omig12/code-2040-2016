# Israel O. Dilan-Pantojas
# israel.dilan@upr.edu
# Code 2040 
# Step 5
import requests
import json
from datetime import *

# Initialize Dictionary
data = {'token':'c13b0b5d48c020b2804774cf748765f7'}

# Request string from API endpoint
r = requests.post('http://challenge.code2040.org/api/dating', json = data)

# Review API response
print r.status_code
if (r.status_code != 200):
	print ("Something weird with status code " + r.status_code + "is going on.")
else:
	print r.text

# Converts JSON formatted string to python dictionary 
dictionary = json.loads(r.text)

# Separate datestamp from Dictionary
datestamp = dictionary['datestamp']

# Separate the interval from Dictionary
interval = dictionary['interval']

# Convert datastamp into a datetime object and add the interval 
t = datetime.strptime(datestamp,"%Y-%m-%dT%H:%M:%SZ") + timedelta(seconds =interval)

# Encode and Add modified date to JSON object  
data['datestamp'] = t.strftime("%Y-%m-%dT%H:%M:%SZ")

# Validate result
r2 = requests.post('http://challenge.code2040.org/api/dating/validate', json = data)

# Review API validation response
print r2.status_code
if (r2.status_code != 200):
	print ("Something weird with status code " + r2.status_code + "is going on.")
else:
	print r2.text