#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get data from fields
year = int(form.getvalue('year'))


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Leap Year</title>")
print ("</head>")
print ("<body>")
print("<h1>This page will tell you if year {} is leap or regular".format(year))

if year % 4 == 0 and not year%100 == 0 or year%400 == 0:
	print('<h2>It appears that year {} is a leap year!</h2>'.format(year))
else:
	print('<h2>It appears that year {} is a leap year!</h2>'.format(year))

print ("</body>")
print ("</html>")


## input a line of a few words through input field and count the number of letters and the number of words
## split()
