#!/usr/bin/python3

import cgi, cgitb 
import json

form = cgi.FieldStorage() 
nameparameter = form.getvalue('name')

isfound = False

with open('/home/ubuntu/files/students.txt', "r") as infile:
	for line in infile:
		name, age, score = line.strip().split(',')
		if name==nameparameter:
			isfound = True
			break

if isfound:
	datastr = json.dumps({"name":name, "age":age, "score":score})
else:
	datastr = json.dumps({"error":"Name not found"})


print("Content-type: application/json")
print ()

print(datastr)

#http://3.68.88.209/cgi-bin/get_students_byname.py?name=Alice