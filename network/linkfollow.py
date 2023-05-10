
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter link:')
reps = int(input('Repetitions:'))
pos = int(input('Position:')) - 1

for i in range(reps):
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  tag = tags[pos]
  url = tag.get('href', None)
  print('Retrieving: ', url)