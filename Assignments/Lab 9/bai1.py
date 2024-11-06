import urllib.request
from urllib.error import URLError, HTTPError

url = 'https://www.google.com/'

try:
    # Attempt to open the URL
    response = urllib.request.urlopen(url)
    content = response.read()

    # Save the content to an HTML file
    with open('result.html', 'wb') as file:
        file.write(content)
    
    print("Content saved successfully in 'result.html'.")
except HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")
except URLError as e:
    print(f"URLError: {e.reason}")