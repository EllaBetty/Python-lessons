#!/usr/bin/python3

#shebang line must be always the first line in the executable CGI script

# we want a script that will return all the data from file as python dictionary (JSON format)

# Import modules for CGI handling 
import cgi, cgitb 
import json

datadict = {names:[], ages:[], scores:[]}

with open('/home/ubuntu/files/students.txt', "r") as infile:
	for line in infile:
		name, age, score = line.strip().split(',')
		datadict['names'].append(name)
		datadict['ages'].append(age)
		datadict['scores'].append(score)


datastr = json.dumps(datadict)


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Students Input</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello user! </h2>")
print ("<h4>{}</h4>".format(datastr))
print ("</body>")
print ("</html>")



## http://3.68.88.209/cgi-bin/students.py?name=Charlie&age=33&score=3.3
## d rwx rwx r-x

