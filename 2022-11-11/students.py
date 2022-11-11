#!/usr/bin/python3

#shebang line must be always the first line in the executable CGI script

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

name = form.getvalue('name')
age  = form.getvalue('age')
score  = form.getvalue('score')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Students Input</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello {}</h2>".format(name))
print ("</body>")
print ("</html>")

#with open('/home/ubuntu/files/students.txt', "a") as file:
#	file.write("{},{},{}\n".format(name, age, score))

## http://3.68.88.209/cgi-bin/students.py?name=Charlie&age=33&score=3.3

