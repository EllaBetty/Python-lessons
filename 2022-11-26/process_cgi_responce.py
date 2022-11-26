
import urllib.request, json

inputname = "Greg"


req = urllib.request.Request('http://3.68.88.209/cgi-bin/get_students_byname.py?name={}'.format(inputname))
response = urllib.request.urlopen(req) 
result = response.read().decode('utf-8')
data = json.loads(result)

##print(data)
if "error" in data:
	print("Something went wrong: ", data["error"])

else:
	print("The student was found")
	print("The name is {}, the age is {} and the score is {}".format(data["name"], data["age"], data["score"]))


## NEXT: Make a script that will take directory path as parameter and give statistics about files found there