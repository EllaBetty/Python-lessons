'''
Weather from Internet
urllib - a module (library) to get information
from the Internet
URL - Universal Resource Locater
universal way to give resource (information)
address on the Net
http - HyperText Transport Protocol
JSON - JavaScript Object Notation
Universally accepted format to send data through Internet
It reminds (and works like) dictionaries in Python
'''
import urllib.request, json


city='Boston'
language='jp'
req = urllib.request.Request('http://api.apixu.com/v1/current.json?key=92d6aec9bef447e3b2b91431170405&q={}&lang={}'.format(city, language))
response = urllib.request.urlopen(req) 
result = response.read().decode('utf-8')
data = json.loads(result)
#data is a dictionary-like object
print('\nThe place')
print(data['location']['country'])
print(data['location']['name'])
print(data['location']['localtime'])
print('\nThe weather there right now')
print(data['current']['temp_c'])
print(data['current']['wind_kph'])


'''
print('\nWeather for the next days')
#Future weather forecast
city = 'Moscow'
days = '3'
req = urllib.request.Request('http://api.apixu.com/v1/forecast.json?key=92d6aec9bef447e3b2b91431170405&q={}&days={}'.format(city, days))
response = urllib.request.urlopen(req) 
result = response.read().decode('utf-8')
data = json.loads(result)
#print(data)
print(data['forecast']['forecastday'][1]['date'])

'''
'''
req = urllib.request.Request('http://www.bbc.com/') #describe, what we want to get
response = urllib.request.urlopen(req)  # get it!
result = response.read().decode('utf-8') # decode it (understand it!)
print(result)
'''
