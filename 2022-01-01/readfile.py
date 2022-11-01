#!/usr/bin/python3
import cgi
import cgitb

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Read and output a text file</title>')
print ('</head>')
print ('<body>')

with open('/home/ubuntu/text.txt', "r") as file:
	for line in file:
		print("<p>"+line+"</p>")

print ('</body>')
print ('</html>')