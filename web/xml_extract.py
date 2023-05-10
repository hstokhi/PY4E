import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL:')
url = urllib.request.urlopen(link, context=ctx)
data = url.read()
print('Retrieved', len(data), 'characters')
data.decode()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count:', len(counts))
comments = 0
for count in counts:
  comment = int(count.text)
  comments = comments + comment

print('Sum:', comments)  