import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL:')
url = urllib.request.urlopen(link, context=ctx)
data = url.read()
print('Retrieved', len(data), 'characters')
data = data.decode()

info = json.loads(data)
print('Count', len(info['comments']))
comments = 0
for item in info["comments"]:
  comment = item["count"]
  comments += comment
print('Sum', comments)