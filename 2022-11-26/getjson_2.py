#!/usr/bin/python3

#shebang line must be always the first line in the executable CGI script

# we want a script that will return all the data from file as python dictionary (JSON format)

# Import modules for CGI handling 
import cgi, cgitb 
import json

print("Content-type: application/json")
#print ()
response={'Price':54,'Cost':'99'}
print(json.dumps(response))