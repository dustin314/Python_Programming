import urllib.request 
url_google = urllib.request.urlopen('http://python.org/') 
html = url_google.read() 