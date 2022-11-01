'''
Create a program that will maintain a simple database of students

Name, Age, Score

This program will input a new student from HTML form and add the record to the database

Alice,24,4.7
Bob,23,4.4
Charlie,21,4.1

'''

#!/usr/bin/python3

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

with open('/home/ubuntu/files/students.txt', "a") as file:
	file.write("{},{},{}\n".format(name, age, score))

