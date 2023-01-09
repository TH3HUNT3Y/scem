import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.random(1024))

# Prompt the user for the location of the names.json file and the URL of the website
names_file = input('Enter the location of the names.json file: ')
url = input('Enter the URL of the website: ')

names = json.loads(open(names_file).read())

# Read the list of proxy URLs from a file
proxies = []
with open('proxies.txt', 'r') as f:
  for line in f:
    line = line.strip()
    proxies.append(line)

# Shuffle the list of proxies to randomize the order
random.shuffle(proxies)

for name in names:
  name_extra = ''.join(random.choice(string.digits))

  username = name.lower() + name_extra + '@yahoo.com'
  password = ''.join(random.choice(chars) for i in range(10))

  # Try each proxy in the list until the request succeeds or you run out of proxies
  for proxy in proxies:
    try:
      # Set the proxy for the request
      response = requests.post(url, allow_redirects=False, data={
        'auid2yjauysd2uasdasdasd': username,
        'kjauysd6sAJSDhyui2yasd': password
      }, proxies={'http': proxy, 'https': proxy})
      # If the request succeeded, break out of the loop
      break
    except:
      # If the request failed, move on to the next proxy
      continue

  print ('sending username %s and password %s') % (username, password)
