#https://repl.it/talk/learn/Using-Web-APIs-in-Python/20777

import urllib.request
import json

# Let's get what the user want to search
search = input("Search: ")
# We will then add that to the url after the search param
url = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=5&format=json&search=" + search

# Let's then open the data we got (it acts like a file) and get the data
req = urllib.request.urlopen(url).read().decode()

# The we can load the json recived from the call
data = json.loads(req)
# Print the data to view it
print(data)
